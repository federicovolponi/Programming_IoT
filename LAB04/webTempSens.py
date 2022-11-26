import cherrypy
import json
import tools

class webTempSens():
    exposed = True
    def __init__(self) -> None:
        self.sensorFile = "sensors.json"    # json file in senML format where sensor is described

    def GET(self, *uri, **query):
        sensorDic = json.load(open(self.sensorFile))
        if uri[0] == "temperature":
            return json.dumps(tools.returnEvent(sensorDic, "temperature"))
        elif uri[0] == "humidity":
            return json.dumps(tools.returnEvent(sensorDic, "humidity"))
        elif uri[0] == "both":
            listEvent = []
            listEvent.append(tools.returnEvent(sensorDic, "temperature"))
            listEvent.append(tools.returnEvent(sensorDic, "humidity"))
            return json.dumps(listEvent)
        else:
            return "Invalid input uri: try with /temperature, /humidity or /both"


if __name__ == "__main__":
    # Standard configuration to serve the url "localhost:8080"
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    webService = webTempSens()
    cherrypy.tree.mount(webService, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()