

class calculator():

    def __init__(self, userInput):
        self.input = userInput
        self.command = ""
        self.values = []
        return

    def add(self, to_addVect):
        pass

    
    def iscommand(self, input):
        if input == "sum":
            return True
        elif input == "sub":
            return True
        elif input == "mul":
            return True
        elif input == "div":
            return True
        elif input == "exit":
            return True 
        else:
            return False    


if __name__ == "__main__":
    userInput = input()
    c = calculator(userInput)
    takevect = False
    for input in c.input:
        if input.isnumeric:
            vect= vect.append(float(input))
