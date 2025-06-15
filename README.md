# 💊 Monitoramento de Temperatura e Umidade para Medicamentos  
### 🔧 Projeto IoT com Arduino e Python

> Um sistema inteligente para garantir a conservação adequada de medicamentos sensíveis, combinando **Arduino** com uma interface gráfica em **Python**.

---

## 🧠 Visão Geral

Medicamentos como **insulina**, **vacinas** e outros produtos farmacêuticos precisam ser armazenados em condições específicas de **temperatura** e **umidade**.  

Este projeto tem como objetivo **monitorar em tempo real** essas condições dentro de uma gaveta ou armário, alertando o usuário em caso de risco — tudo isso com uma interface simples, visual e acessível.

---

## 🔌 Como Funciona?

1. O **Arduino** coleta dados dos sensores de temperatura (**DHT11**) e estado da gaveta (**sensor magnético**).
2. Esses dados são enviados via **porta serial** para o computador.
3. Um programa em **Python** lê essas informações, exibe os dados em tempo real por meio de uma **interface gráfica (GUI)** e os registra em um arquivo `.csv`.
4. Se a temperatura estiver fora do limite (acima de **30°C**), um **alerta visual e sonoro** é exibido para o usuário.

---

## 🛠️ Tecnologias Utilizadas

### 🔽 Hardware (Arduino)

- 🟦 **Arduino UNO**
- 🌡️ **Sensor DHT11** – para medir temperatura e umidade
- 🧲 **Sensor Magnético De Efeito Hall Ky-003** – para detectar a abertura da gaveta
- 🖥️ **Display LCD 16x2 com interface I2C**
- 🔌 **Cabo USB** – para comunicação com o computador

### 💻 Software (Python)

- 🐍 **Python 3.8+**
- 📦 Bibliotecas Python utilizadas:
  - `tkinter` – criação da interface gráfica (GUI)
  - `matplotlib` – gráficos em tempo real
  - `pandas` – manipulação e salvamento de dados em `.csv`
  - `pyserial` – comunicação com a porta serial do Arduino

---

## 🖥️ Interface do Usuário

- ✅ **Temperatura Atual**: exibida em tempo real, com variação de cores
- 🔓 **Estado da Gaveta**: mostra se está **aberta** ou **fechada**, com alerta piscante
- 📉 **Gráfico em tempo real**: temperatura vs. tempo (últimos 20 registros)
- 🚨 **Alerta visual**: se a temperatura ultrapassar 30 °C

---

## 📈 Exemplo de Uso

1. Conecte o **Arduino** via USB.
2. Execute o script Python:
   ```bash
   python monitoramento_gaveta_med.py


🤝 Contribuições
Sinta-se à vontade para clonar, adaptar e melhorar este projeto!
Pull requests são bem-vindos. 😉