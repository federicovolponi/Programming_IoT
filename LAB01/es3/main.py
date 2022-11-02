import json
import time

def searchByName(name):
    devicesList = fileDic.get("devicesList")
    for dic in devicesList:
        if dic.get("deviceName") == name:
            print(dic)
            return
    print("Device not found")

def searchByID(id):
    devicesList = fileDic.get("devicesList")
    for dic in devicesList:
        if dic.get("deviceID") == id:
            print(dic)
            return
    print("Device not found")

def searchByService(services):
    dicService ={}
    devicesList = fileDic.get("devicesList")
    for dic in devicesList:
        noservice = False
        dicService ={}
        for service in services:
            if dic.get("availableServices").count(service) == 0:
                noservice = True
                break
            else:
                dicService = dic
        if not noservice:
            print(dicService)

def searchByMeasureType(measures):
    dicMeasure ={}
    devicesList = fileDic.get("devicesList")
    for dic in devicesList:
        nomeasure = False
        dicMeasure ={}
        for measure in measures:
            if dic.get("measureType").count(measure) == 0:
                nomeasure = True
                break
            else:
                dicMeasure = dic
        if not nomeasure:
            print(dicMeasure)

def insertDevice(id):
    #devicesList = fileDic.get("devicesList")
    if fileDic.get("deviceID").count(id) > 0:
        #update
        pass
    else:
        #insert
        pass   

if __name__ == "__main__":
    file_name = "/home/federico/Coding/Programming_IoT/LAB01/es3/catalog.json"
    fileDic = json.load(open(file_name))
    #searchByName("pi")
    #searchByID(4)
    #searchByService(["MQTT"])
    searchByMeasureType(["Temperature", "Humidity"])