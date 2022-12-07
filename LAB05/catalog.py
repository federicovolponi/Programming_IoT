import json

class catalog():
    def __init__(self):
        self.filename = "LAB05/catalog.json"
        self.jsonDic = json.load(open(self.filename))
        self.deviceTempl = {
            "deviceID": 0,
            "deviceName": "",
            "measureType": [],
            "availableServices": [
            ],
            "servicesDetails": [
                {
                    "serviceType": "MQTT",
                    "topic": [
                        "MySmartThingy/1/temp",
                        "MySmartThingy/1/hum"
                    ]
                },
                {
                    "serviceType": "",
                    "serviceIP": ""
                }
            ],
            "lastUpdate": ""
        }
        #self.fileWrit = open(self.filename, "w")
    
    def brokerInfo(self):
        ip = self.jsonDic["broker"]["ip"]
        port = self.jsonDic["broker"]["port"]
        return ip, port
    def addDevice(self, newDevice):
        fw = open(self.filename, "w")
        self.jsonDic["devicesList"].append(newDevice)
        json.dump(self.jsonDic, fw, indent=4)