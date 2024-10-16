#declarando bibliotecas
import time
import board
import busio
import adafruit_adxl34x #biblioteca del acelerómetro

#Iniciando la comunicación i2C
i2c = busio.I2C(board.SCL, board.SDA)
mide = adafruit_adxl34x.ADXL345(i2c)

while True:
    print("%f %f %f"%mide.acceleration)
    time.sleep(1)
