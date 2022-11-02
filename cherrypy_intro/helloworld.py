import cherrypy
class HelloWorld(object):
	exposed=True
	def GET(self,*uri,**params):
		#Standard output
		output="Hello World"
		#Check the uri in the requests
		#<br> is just used to append the content in a new line
		#<br> is the \n for HTML)
		if len(uri)!=0:
			str_uri = uri[0]
			output += '<br>' + f"{str_uri[::-1]}" 
			
		#Check the parameters in the request
		#<br> is just used to append the content in a new line
		#<br> is the \n for HTML)
		if params!={}:
			output+='<br>params: '+str(params)

		
		return output

	def POST(self, *uri, **params):
		pass
		

if __name__ == "__main__": #Standard configuration to serve the url "localhost:8080"
	
	conf={
		'/':{
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tool.session.on': True
		}
	}
	webService=HelloWorld()
	cherrypy.tree.mount(webService,'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()