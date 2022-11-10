import paho.mqtt.client as PahoMQTT
import json
from MyMQTT import *
import time


class Led:
    def __init__(self, clientID, broker, topic):
        self.clientID = clientID
        self.broker = broker
        self.topic = topic
        self.ckient = MyMQTT(self.clientID, self.broker, 1883, self)
        self.status = 'off'

    def startOperation(self):
        self.client.start()
        time.sleep()
        self.client.mySubscribe(self.topic)
    
    def notify(self, topic, payload):
        #{"staus":value}
        self.status = json.loads(payload['status'])
        print(f'the led isn{self.status}')

if __name__ == "__main__":
    led = Led("Gon", "mqtt.eclipseprojects.io","?")
    

        