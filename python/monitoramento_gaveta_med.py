import serial
import time
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

PORTA_SERIAL = 'COM6'
BAUD_RATE = 9600

arquivo_log = 'log_temperatura.csv'
df_log = pd.DataFrame(columns=['DataHora', 'Temperatura', 'Gaveta'])

try:
    arduino = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
    time.sleep(2)
except Exception as e:
    print("Erro ao conectar na porta serial:", e)
    exit()

root = tk.Tk()
root.title("Monitoramento")

label_temp = ttk.Label(root, text="Temperatura: -- °C", font=("Arial", 16))
label_temp.pack(pady=10)

label_gaveta = ttk.Label(root, text="Gaveta: ---", font=("Arial", 16))
label_gaveta.pack(pady=10)

fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
toolbar.pack()

tempos = []
temperaturas = []

alerta_exibido = False
gaveta_aberta = False
cor_gaveta = "black"

def piscar_gaveta():
    global cor_gaveta
    if gaveta_aberta:
        nova_cor = "red" if cor_gaveta == "black" else "black"
        cor_gaveta = nova_cor
        label_gaveta.config(foreground=nova_cor)
        root.after(500, piscar_gaveta)
    else:
        label_gaveta.config(foreground="black")

def atualizar_dados():
    global df_log, alerta_exibido, gaveta_aberta

    try:
        linha = arduino.readline().decode('utf-8').strip()

        estado_gaveta = "---"
        temperatura = None

        if ";" in linha:
            partes = linha.split(";")
            for parte in partes:
                parte = parte.strip()
                if parte.startswith("Gaveta:"):
                    estado_gaveta = parte.split(":")[1].strip()
                elif parte.startswith("Temp:"):
                    temp_str = parte.split(":")[1].replace("C", "").replace("°", "").strip()
                    try:
                        temperatura = float(temp_str)
                    except ValueError:
                        temperatura = None

        if temperatura is not None:
            agora = datetime.now().strftime("%H:%M:%S")

            label_temp.config(text=f"Temperatura: {temperatura:.1f} °C")
            label_gaveta.config(text=f"Gaveta: {estado_gaveta}")

            if estado_gaveta.lower() == "aberta":
                if not gaveta_aberta:
                    gaveta_aberta = True
                    piscar_gaveta()
            else:
                gaveta_aberta = False
                label_gaveta.config(foreground="black")

            temperaturas.append(temperatura)
            tempos.append(agora)
            if len(tempos) > 20:
                temperaturas.pop(0)
                tempos.pop(0)

            ax.clear()
            ax.plot(tempos, temperaturas, marker='o', color='red' if temperatura > 30 else 'blue')
            ax.set_title("Temperatura")
            ax.set_ylabel("°C")
            ax.tick_params(axis='x', rotation=45)
            fig.tight_layout()
            canvas.draw()

            if temperatura > 30 and not alerta_exibido:
                alerta_exibido = True
                messagebox.showwarning("Alerta de Temperatura", f"Temperatura alta: {temperatura:.1f} °C\nAjuste o ambiente!")

            if temperatura <= 30:
                alerta_exibido = False

            df_log.loc[len(df_log)] = [agora, temperatura, estado_gaveta]
            df_log.to_csv(arquivo_log, index=False)

    except Exception as e:
        print("Erro:", e)

    root.after(2000, atualizar_dados)

atualizar_dados()
root.mainloop()
