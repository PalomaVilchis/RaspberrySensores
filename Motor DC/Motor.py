import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1 = 16    # Entrada
Motor2 = 18    # Entrada
Motor3 = 22    # Habilitar

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)

print ("Adelante")
GPIO.output(Motor1,GPIO.HIGH)
GPIO.output(Motor2,GPIO.LOW)
GPIO.output(Motor3,GPIO.HIGH)

sleep(3)

print ("Atras")
GPIO.output(Motor1,GPIO.LOW)
GPIO.output(Motor2,GPIO.HIGH)
GPIO.output(Motor3,GPIO.HIGH)

sleep(3)

print ("Detener")
GPIO.output(Motor3,GPIO.LOW)

GPIO.cleanup()
