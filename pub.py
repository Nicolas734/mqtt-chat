import paho.mqtt.client as mqtt
from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")

broker = config["MQTT"]["broker"] or None
topic = config["MQTT"]["topic"] or None
user = config["USER"]["name"] or None


if not broker:
	broker = str(input("Digite o broker: "))

if not topic :
	topic = str(input("Digite o topico: "))

if not user:
	user = str(input("Digite o seu nome: "))


print("Entrando no chat...")
con = mqtt.Client()
con.connect(broker, 1883, 60)

con.loop_start()

while True:
	msg = input("Envie uma mensagem: ")
	infos = {"user": user, "msg": msg}
	con.publish(topic,str(infos))