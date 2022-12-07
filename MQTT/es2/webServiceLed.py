import cherrypy
import json
import LedPublisher as ld

class webLed():
    exposed = True
    def __init__(self):
        self.led = ld.LedManeger("fedeRICO9911","mqtt.eclipseprojects.io","iot/federico/led")
        self.led.startOperation()
    def GET(self, *uri, **query):
        return open("index.html")
    def PUT(self, *uri, **query):
        self.led.setledstatus(uri[0])
        return
if __name__ == "__main__":
    # Standard configuration to serve the url "localhost:8080"
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }
    webService = webLed()
    cherrypy.tree.mount(webService, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()

