def start(client, args=None):
    client.on_message = on_message
    client.subscribe(
        "common", #채널, 토픽
        1, #QoS
    )
    client.loop_forever()

def on_message(client, userdata, message):
    payload = message.payload.decode("UTF-8")
    print(f"Topic[{message.topic}]: {payload}")
