#sudo pip3 install adafruit-circuitpython-dht
#sudo apt-get install libgpiod2
#ejecutar en terminal como sudo python3 nombre.py

import Adafruit_DHT  
import time  

while True:
  sensor = Adafruit_DHT.DHT11 
  pin = 4
  humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

  print ('Humedad: ' , humedad)
  print ('Temperatura: ' , temperatura)
 
  time.sleep(1)
