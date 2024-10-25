import time
import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid, reason_code, properties):
    
    try:
        userdata.remove(mid)
    except KeyError:
        print("No hay conexión")

#Establecer conexion
unacked_publish = set()
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_publish = on_publish

mqttc.user_data_set(unacked_publish)
#definir broker y puerto de conexion
mqttc.connect("broker.hivemq.com", 1883)

mqttc.loop_start()

# Publicando mensajes en el topic
msg_info = mqttc.publish("testTECIoT/2", "raspberry Pi 3", qos=2)
unacked_publish.add(msg_info.mid)

msg_info2 = mqttc.publish("testTECIoT/2", "Hola grupo", qos=2)
unacked_publish.add(msg_info2.mid)

# Espera publicando minsaje
while len(unacked_publish):
    time.sleep(0.1)

# En espera de la conexion y publicación segura
msg_info.wait_for_publish()
msg_info2.wait_for_publish()

mqttc.disconnect()
mqttc.loop_stop()

