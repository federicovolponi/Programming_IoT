import json
import paho.mqtt.client as PahoMQTT
from MyMQTT import *
import time

class subTempSens:
    def __init__(self, clientID, broker, topic):    #clientID must be unique, different from subscribers
        self.broker = broker
        self.topic = topic
        self.clientID = clientID
        self.client = MyMQTT(self.clientID, self.broker,1883,self) #the last self is the client that take work of the notifier

    def startOperation(self):
        self.client.start()
        time.sleep(3) #we want to be sure to do that commands in order
        self.client.mySubscribe(self.topic)


    def notify(self,topic,payload):
        #{"status":value}
        self.temperature=json.loads(payload) #load the payload and take the status
        print(f"{self.temperature}")

if __name__ == "__main__":
    sensor = subTempSens("fedeRICO99","mqtt.eclipseprojects.io","iot/federico/+")
    sensor.startOperation()
    while True:
        time.sleep(3)