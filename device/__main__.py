import paho.mqtt.client as mqtt
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

from device.run import start

client = mqtt.Client()

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
start(client)
client.disconnect()
