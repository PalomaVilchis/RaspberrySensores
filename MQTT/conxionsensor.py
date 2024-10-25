import time
import board
import adafruit_bmp280
import paho.mqtt.client as mqtt


i2c = board.I2C() 
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)


bmp280.sea_level_pressure = 1013.25

def on_publish(client, userdata, mid, reason_code, properties):
   
    try:
        userdata.remove(mid)
    except KeyError:
        print("Error")
 

unacked_publish = set()
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_publish = on_publish

mqttc.user_data_set(unacked_publish)
mqttc.connect("broker.hivemq.com", 1883)

mqttc.loop_start()

# Publicar en topic 1
msg_info = mqttc.publish("testTECIoT/2", "\nTemperatura: %0.1f C" % bmp280.temperature, qos=2)
unacked_publish.add(msg_info.mid)

# Publicar en topic 2
msg_info2 = mqttc.publish("testpalo/2", "profe", qos=2)
unacked_publish.add(msg_info2.mid)

# Esperando a publicar el mensaje
while len(unacked_publish):
    time.sleep(0.1)

msg_info.wait_for_publish()
msg_info2.wait_for_publish()

mqttc.disconnect()
mqttc.loop_stop()

    

