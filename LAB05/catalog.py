import json

class catalog():

    def __init__(self):
        self.filename = "LAB05\catalog.json"    #file's json name
        self.jsonDic = json.load(open(self.filename))   #load json file into a dictionary
        
    # Method to receive broker's information
    def brokerInfo(self):
        ip = self.jsonDic["broker"]["ip"]
        port = self.jsonDic["broker"]["port"]
        return ip, port

    # Method to receive devices information (ids can be specified)
    def devicesInfo(self, id=[]):
        devices = self.jsonDic["devicesList"]   
        if len(id) != 0:    #check if ids are selected
            idDevices = []
            for device in devices:
                if id.count(device.get('deviceID')) != 0:   
                    idDevices.append(device)
            return idDevices    #return the id selected devices
        return devices  #return all the devices

    def addDevice(self, newDevice):
        fw = open(self.filename, "w")
        self.jsonDic["devicesList"].append(newDevice)
        json.dump(self.jsonDic, fw, indent=4)