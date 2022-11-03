import json
import cherrypy


class HelloWorld(object):
    exposed = True

    def GET(self, *uri):
        string = uri[0]
        reversed = string[::-1]
        return reversed

    def POST(self):
        bodyAsString = cherrypy.request.body.read()
        bodyAsDictionary = json.loads(bodyAsString)
        for k in bodyAsDictionary.keys():
            bodyAsDictionary[k] = bodyAsDictionary[k][::-1]
        return json.dumps(bodyAsDictionary)


if __name__ == "__main__":
    # Standard configuration to serve the url "localhost:8080"
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }
    webService = HelloWorld()
    cherrypy.tree.mount(webService, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
