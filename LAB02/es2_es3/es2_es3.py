import calculator as calc
import cherrypy
import json

class webCalculator():
    exposed = True

    def GET(self, *uri, **query):
        
        user_input = str()
        for inp in uri:
            user_input += inp + " " 
        
        c = calc.calculator(user_input)
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

    def PUT(self, *uri, **query):
        bodyAsString = cherrypy.request.body.read()
        bodyAsDictionary = json.loads(bodyAsString)
        user_input = bodyAsDictionary['command']
        for value in bodyAsDictionary['operands']:
            user_input += " " + str(value)
        c = calc.calculator(user_input)
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
        return json.dumps(c.listDict)

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

