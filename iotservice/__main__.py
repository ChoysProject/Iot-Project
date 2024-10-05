import paho.mqtt.client as mqtt
from iotservice import subscribe as sub

client = mqtt.Client()

# callback 함수 지정
client.on_connect = sub.on_connect
client.on_disconnect = sub.on_disconnect
client.on_subscribe = sub.on_subscribe

from iotservice import processor

client.connect("localhost", 1883)  #localhost등
processor.start(client)
