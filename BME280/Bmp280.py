#Creditos: https://pypi.org/project/bmp-280/

import time
import board
import adafruit_bmp280


i2c = board.I2C() 
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)


bmp280.sea_level_pressure = 1013.25

while True:
    print("\nTemperatura: %0.1f C" % bmp280.temperature)
    print("Presioón: %0.1f hPa" % bmp280.pressure)
    print("Altitud = %0.2f metros" % bmp280.altitude)
    time.sleep(2)
