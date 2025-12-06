import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("test.mosquitto.org", 1883, 60)

client.publish("Asgard/power", "100W")
client.publish("Asgard/temperature", "20C")
client.publish("Asgard/humidity", "50%")
client.publish("Asgard/pressure", "1013hPa")

client.disconnect()
