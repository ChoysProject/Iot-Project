import paho.mqtt.client as mqtt
from iotsensor import publish as pub

# client = mqtt.Client()
# 프로토콜 버전 명시 방법
client = mqtt.Client(protocol=mqtt.MQTTv311, transport="tcp")

# callback 함수 지정
client.on_connect = pub.on_connect
client.on_disconnect = pub.on_disconnect
client.on_publish = pub.on_publish

from iotsensor import sensor
import ssl

client.tls_set(
    "ca.pem",
    certfile="thing.crt",
    keyfile="thing.key",   
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLSv1_2,
    ciphers=None
)
client.connect("a1ztynhdwt5f6d-ats.iot.ap-northeast-2.amazonaws.com", 8883)  #localhost등
# 문서 https://github.com/eclipse/paho.mqtt.python 살펴보기
# AWS 사용시
# client.tls_set(
#    "ca.pem",
#    certfile="thing.crt",
#    keyfile="thing.key",
#    cert_reqs=ssl.CERT_REQUIRED,
#    tls_version=ssl.PROTOCOL_TLSv1_2,
#    ciphers=None
# )
# client.connect("아마존의 IOT 주소", 8883)

sensor.start(client)
client.disconnect()
