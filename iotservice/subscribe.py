def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected OK")
    else:
        print(f"Bad connection returned code={rc}")

def on_disconnect(client, userdata, flags, rc=0):
    print(f"Disconneted(code={rc})")

def on_subscribe(client, userdata, mid, qos):
    print(f"Subscribed: "
        f"Message ID={mid}: QoS={qos}")
