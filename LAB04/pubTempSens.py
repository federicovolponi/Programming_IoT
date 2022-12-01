from MyMQTT import *
import time
import tools
import json

class pubTempSens():
    def __init__(self, clientID, broker, topic):
        self.broker = broker
        self.topic = topic
        self.clientID = clientID
        self.client = MyMQTT(self.clientID, self.broker,1883,self) #the last self is the client that take work of the notifier
        self.file = "sensors.json"
        return

    def startOperation(self):
        self.client.start()
        time.sleep(3) #we want to be sure to do that commands in order
    
    def pubEvent(self):
        sensorDic = json.load(open(self.file))
        temp = tools.returnEvent(sensorDic, "temperature")
        self.client.myPublish("iot/federico/temperature", temp)
        hum = tools.returnEvent(sensorDic, "humidity")
        self.client.myPublish(self.topic, hum)
        both = [temp, hum]
        self.client.myPublish(self.topic, both)
        
if __name__ == "__main__":
    sensor = pubTempSens("fedeRICO9911","mqtt.eclipseprojects.io","iot/federico/")
    sensor.startOperation()
    while 1:
        sensor.pubEvent()
        time.sleep(5)