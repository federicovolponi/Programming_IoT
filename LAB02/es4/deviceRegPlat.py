import cherrypy
import json
import os
class deviceRegPlat():
    exposed = True
    def __init__(self):
        self.filepath = "devices.json"
    
    def GET(self, *uri, **params):
        return open("index.html")
    
    def POST(self, *uri, **params):
        InputAsString = cherrypy.request.body.read()
        InputAsDict = json.loads(InputAsString)
        
        if os.stat(self.filepath).st_size != 0:
            listDict = json.load(open(self.filepath))
        listDict["devicesList"].append(InputAsDict)
        json.dump(listDict,  open(self.filepath, "w"))

        return json.dumps(listDict)