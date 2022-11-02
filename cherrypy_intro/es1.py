import cherrypy


class HelloWorld(object):
    exposed = True

    def GET(self, *uri):
        string = uri[0]
        reversed = string[::-1]
        return reversed


if __name__ == "__main__":
    # Standard configuration to serve the url "localhost:8080"
    conf={
		'/':{
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tool.session.on': True
		}
	}
    webService = HelloWorld()
    cherrypy.tree.mount(webService, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
