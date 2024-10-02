import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
print("medición en progreso")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)
print("esperando datos")
time.sleep(2)

GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)

while GPIO.input(ECHO)==0:
	pulse_start=time.time()
	
while GPIO.input(ECHO)==1:
	pulse_end=time.time()
	
pulso_dura=pulse_end - pulse_start

dist = pulso_dura * 17150
dist= round (dist, 2)
print("La distancia medida es:",dist,"cm")
GPIO.cleanup()
