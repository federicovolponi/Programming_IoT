import deviceRegPlat as dev
import os
import cherrypy

if __name__ == "__main__":
	# Standard configuration to serve the url "localhost:8080"
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tools.staticdir.root': os.path.abspath(os.getcwd()),
			},
		 '/css':{
		 'tools.staticdir.on': True,
		 'tools.staticdir.dir':'./css'
		 },
		 '/js':{
		 'tools.staticdir.on': True,
		 'tools.staticdir.dir':'./js'
		 },
	}	
	webService = dev.deviceRegPlat()
	cherrypy.tree.mount(webService,'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()