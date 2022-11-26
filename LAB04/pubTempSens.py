import MyMQTT
import time
import tools

class pubTempSens():
    def __init__(self, clientID, broker, topic):
        self.broker = broker
        self.topic = topic
        self.clientID = clientID
        self.client = MyMQTT(self.clientID, self.broker,1883,self) #the last self is the client that take work of the notifier
        return

    def startOperation(self):
        self.client.start()
        time.sleep(3) #we want to be sure to do that commands in order
    
    def pubEvent(self, sensorDic):
        tools.re
        self.client.myPublish(self.topic, )
if __name__ == "__main__":
    while 1:

        time.sleep(5)