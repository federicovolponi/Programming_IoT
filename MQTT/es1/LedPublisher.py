import json
import paho.mqtt.client as PahoMQTT
from MyMQTT import *
import time

class LedManeger:
    def __init__(self, clientID, broker, topic):
        self.broker = broker
        self.topic = topic
        self.clientID = clientID
        self.client = MyMQTT(self.clientID, self.broker,1883,self) #the last self is the client that take work of the notifier

    def startOperation(self):
        self.client.start()
        time.sleep(3) #we want to be sure to do that commands in order
    
    def setledstatus(self,status):
        msg={'status':status}
        self.client.myPublish(self.topic,msg)

if __name__ == "__main__":
    led = LedManeger("fedeRICO9911","mqtt.eclipseprojects.io","iot/federico/led")
    led.startOperation()
    c=0
    while c<30:
        if c%2==0:
            led.setledstatus('on')
        else:
            led.setledstatus('off')
        c+=1
        time.sleep(5)