import calculator
import cherrypy

class webCalculator():
    exposed = True

    def GET(self, *uri, **query):
        
        values = []
        user_input = str(uri[0])
        for key in query:
            values.append(query[key])
            user_input += " " + str(query[key])
        
        c = calculator(user_input)
        vect = []
        for word in (c.input.split()+(["EOF"])):
            isdigit = word.isdigit()
            if isdigit:
                vect.append(float(word))
            else:
                if len(vect) != 0:
                    c.values = vect
                    c.add()
                    c.sub()
                    c.div()
                    c.mul()
                    vect = []
                c.iscommand(word)
        return c.res

if __name__ == "__main__":
    # Standard configuration to serve the url "localhost:8080"
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }
    webService = webCalculator()
    cherrypy.tree.mount(webService, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()

