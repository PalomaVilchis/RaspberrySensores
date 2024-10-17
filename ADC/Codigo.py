import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


i2c = busio.I2C(board.SCL, board.SDA)


ads = ADS.ADS1115(i2c)

# Define el canal de lectura
channel = AnalogIn(ads, ADS.P0)

# Lectura continua
while True:
    print("Valor analogico: ", channel.value, "Volts: ", channel.voltage)
    time.sleep(0.5)
