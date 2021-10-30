import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
led=40
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led, GPIO.LOW)
reader = SimpleMFRC522()
while True:
        try:

            id, text = reader.read()
            print(id)
            print(type(id))
            print(text)
            sleep(2)

            if id==872589727:
                sleep(2)
                GPIO.output(led, GPIO.HIGH)
                sleep(1)
            else:
                GPIO.output(led, GPIO.LOW)
        except:
                GPIO.cleanup()
