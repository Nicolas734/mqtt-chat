import paho.mqtt.client as mqtt
from configparser import ConfigParser
import json


config = ConfigParser()
config.read("config.ini")

topic = config["MQTT"]["topic"] or None
broker = config["MQTT"]["broker"] or None

def on_connect(con, userdata, flags, rc):
    print("Chat iniciado com sucesso")
    con.subscribe(topic)

def on_message(con, userdata, msg):
    payload = convert_bytes_to_json(msg.payload)
    print(payload["user"] + ": " + payload["msg"])

def convert_bytes_to_json(value):
    decode = value.decode().replace("'", '"')
    response = json.loads(decode)
    return response


if not broker:
	broker = str(input("Digite o broker: "))

if not topic :
	topic = str(input("Digite o topico: "))


print("Iniciando chat")
con = mqtt.Client()
con.on_connect = on_connect
con.on_message = on_message

con.connect(broker, 1883, 60)

con.loop_forever()