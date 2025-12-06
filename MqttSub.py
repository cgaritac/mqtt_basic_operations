import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("Asgard/#")

def on_message(client, userdata, msg):
    if msg.topic == "Asgard/power":
        print("Power: "+str(msg.payload))
    elif msg.topic == "Asgard/temperature":
        print("Temperature: "+str(msg.payload))
    elif msg.topic == "Asgard/humidity":
        print("Humidity: "+str(msg.payload))
    elif msg.topic == "Asgard/pressure":
        print("Pressure: "+str(msg.payload))
    else:
        print("Unknown topic: "+msg.topic)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("test.mosquitto.org", 1883, 60)

mqttc.loop_forever()

