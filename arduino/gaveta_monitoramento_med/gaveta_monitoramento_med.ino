#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

#define DHTPIN 3
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

#define SENSOR_MAGNETICO 2

void setup() {
  lcd.init();
  lcd.backlight();

  dht.begin();
  pinMode(SENSOR_MAGNETICO, INPUT);

  Serial.begin(9600);
}

void loop() {
  int estadoGaveta = digitalRead(SENSOR_MAGNETICO);
  float temperatura = dht.readTemperature();

  if (isnan(temperatura)) {
    lcd.setCursor(0, 0);
    lcd.print("Erro DHT11     ");
    Serial.println("Gaveta: ---; Temp: ERROR");
    delay(2000);
    return;
  }

  lcd.setCursor(0, 0);
  lcd.print("Gaveta: ");
  lcd.print(estadoGaveta == HIGH ? "ABERTA " : "FECHADA");

  lcd.setCursor(0, 1);
  lcd.print("Temp: ");
  lcd.print(temperatura, 1);
  lcd.print((char)223);
  lcd.print("C   ");

  Serial.print("Gaveta: ");
  Serial.print(estadoGaveta == HIGH ? "ABERTA" : "FECHADA");
  Serial.print("; Temp: ");
  Serial.print(temperatura);
  Serial.println("C");

  delay(1000);
}
