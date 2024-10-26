import struct

import paho.mqtt.client as mqtt

client = mqtt.Client()


def on_message(client, userdata, message):
    payload = message.payload
    serial, s1, s2, s3, s4, T, C = struct.unpack(">IBBBBhh", payload)
    active = (s1 >> 7) & 0x1
    battery = s1 & 0x7f
    control = (s2 >> 7) & 0x1
    period = s2 & 0x7f

    print(f"""Topic[{message.topic}]: SERIAL={serial}, BATTERY={battery}%,
                            ACTIVE={active}, CONTROL={control},
                            TARGET={T / 100}, CURRENT={C / 100}""")

    # print(f"Topic[{message.topic}]: Payload={payload}")

    # serial, s1, s2, s3, s4, T, C = struct.unpack(">IBBBBhh", payload)
    # active = (s1 >> 7) & 0x1
    # battery = s1 & 0x7f
    # control = (s2 >> 7) & 0x1
    # period = s2 & 0x7f
    #
    # print(f"""Topic[{message.topic}]: SERIAL={serial}, BATTERY={battery}%,
    #                         ACTIVE={active}, CONTROL={control},
    #                         TARGET={T / 100}, CURRENT={C / 100}""")


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

client.on_message = on_message
client.subscribe("device/1/data", 1)
client.subscribe("device/ping", 1)
client.subscribe("device/register", 1)
client.loop_forever()
