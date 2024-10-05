import json
import time

def start(client, args=None):
    client.loop_start()
    for v in range(10):
        client.publish(
            "$aws/things/ARDUINO_PIR/shadow/name/iot2024/update",   #Topic
            json.dumps({
                "state": {
                    "reported": {
                        "temperature": {"value": 20 + v , "unit": "C"}
                    }
                }
            }), # Message
            1   #QoS
        )
        time.sleep(5)
    client.loop_stop()
