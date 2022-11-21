import json
import paho.mqtt.client as PahoMQTT
from MyMQTT import *
import time

class Led:
    def __init__(self, clientID, broker, topic):    #clientID must be unique, different from subscribers
        self.broker = broker
        self.topic = topic
        self.clientID = clientID
        self.client = MyMQTT(self.clientID, self.broker,1883,self) #the last self is the client that take work of the notifier
        self.status = 'off'

    def startOperation(self):
        self.client.start()
        time.sleep(3) #we want to be sure to do that commands in order
        self.client.mySubscribe(self.topic)


    def notify(self,topic,payload):
        #{"status":value}
        self.status=json.loads(payload)['status'] #load the payload and take the status
        print(f"The led is {self.status}")

if __name__ == "__main__":
    led = Led("fedeRICO99","mqtt.eclipseprojects.io","iot/federico/led")
    led.startOperation()
    while True:
        time.sleep(3)