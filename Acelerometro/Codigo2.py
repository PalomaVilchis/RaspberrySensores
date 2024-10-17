import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accel = adafruit_adxl34x.ADXL345(i2c)
accel.enable_freefall_detection(threshold=10, time=25)
accel.enable_motion_detection(threshold=18)
accel.enable_tap_detection(tap_count=1, threshold=20, duration=50, latency=20, window=255)

while True:
    print("%f %f %f"%accel.acceleration)
    print("Caida Libre: %s"%accel.events["freefall"])
    print("Tap: %s"%accel.events['tap'])
    print("Movimiento detectado: %s"%accel.events['motion'])
    time.sleep(0.5)
