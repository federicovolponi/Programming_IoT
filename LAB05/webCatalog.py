import cherrypy
import json
from catalog import *

class webCatalog():
    exposed = True
    def __init__(self):
        self.catObj = catalog()
    
    def GET(self, *uri, **params):
        if uri[0] == "broker":
            ip, port = self.catObj.brokerInfo()
            toReturn = f"BROKER INFO:\nIP: {ip}\nPORT: {port}"
            return toReturn
    
    def POST(self, *uri, **params):
        bodyAsString = cherrypy.request.body.read()
        bodyAsDictionary = json.loads(bodyAsString)
        if uri[0] == "device":
            self.catObj.addDevice(bodyAsDictionary)
        if uri[0] == "user":
            pass

if __name__ == "__main__": #Standard configuration to serve the url "localhost:8080"
	
	conf={
		'/':{
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True
		}
	}
	webService=webCatalog()
	cherrypy.tree.mount(webService,'/',conf)
    #cherrypy.config.update({'server.socket_port': 8181})
	cherrypy.engine.start()
	cherrypy.engine.block()