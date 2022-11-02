import json

import requests


class DeviceManager:
    def __init__(self, url):
        self.url = url

    def all(self):
        r = requests.get(self.url+"/all")
        output = r.json()
        return json.dumps(output, indent=4)

    def devices(self):
        r = requests.get(self.url+"/devices")
        output = r.json()
        return json.dumps(output, indent=4)

    def houses(self):
        r = requests.get(self.url+"/houses")
        output = r.json()
        return json.dumps(output, indent=4)

    def users(self):
        r = requests.get(self.url+"/users")
        output = r.json()
        return json.dumps(output, indent=4)

def menu(manager):
    while True:
        command = input("Select what u want to see: all, devices, houses, users: ")
        output = "command not found"
        if command == "all":
            output = manager.all()
        elif command == "devices":
            output = manager.devices()
        elif command == "houses":
            output = manager.houses()
        elif command == "users":
            output = manager.users()
        elif command == "quit":
            break
        print(output)


if __name__ == "__main__":
    manager = DeviceManager("https://catalog-p4iot.onrender.com")
    menu(manager)
