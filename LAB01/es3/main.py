import json

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
        dicService ={}
        for service in services:
            if dic.get("availableServices").count(service) == 0:
                break
            else:
                dicService = dic
        if dicService != {}:
            print(dicService)

if __name__ == "__main__":
     file_name = "/home/federico/Coding/Programming_IoT/LAB01/es3/catalog.json"
     fileDic = json.load(open(file_name))
     #searchByName("pi")
     #searchByID(4)
     searchByService(["MQTT", "REST"])