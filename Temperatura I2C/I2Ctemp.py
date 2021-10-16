from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
print ("Temperatura ambiente :", sensor.get_ambient())
print ("Temperatura de Persona u objeto :", sensor.get_object_1())
bus.close() 
