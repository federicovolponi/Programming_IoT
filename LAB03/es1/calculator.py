import json
import numpy as np
import os




class calculator():

    def __init__(self, userInput):
        self.input = userInput
        self.command = ""
        self.values = []
        self.subTrue = False
        self.mulTrue = False
        self.sumTrue = False
        self.divTrue = False
        self.exitTrue = False
        self.listDict = []
        self.res = 0
        self.currentOper = {}
        return


    def json_write(self,file, dictionary):
        if os.stat(file).st_size != 0:
            self.listDict = json.load(open(file))
        self.listDict.append(dictionary)
        json.dump(self.listDict,  open(file, "w"))

    def add(self):
        if self.sumTrue:
            res = np.sum(self.values)
            addDictionary = {"input": self.values,
                             "Operator": "add",
                             "output": res}
            self.json_write("calculator.json", addDictionary)
            self.res = res
            self.currentOper = addDictionary
            print(res)

    def sub(self):
        if self.subTrue:
            res = self.values[0] - sum(self.values[1:])
            addDictionary = {"input": self.values,
                             "Operator": "sub",
                             "output": res}
            self.json_write("calculator.json", addDictionary)
            self.res = res
            self.currentOper = addDictionary
            print(res)
    
    def mul(self):
        if self.mulTrue:
            res = 1
            for x in self.values:
                res = res * x
            addDictionary = {"input": self.values,
                             "Operator": "mul",
                             "output": res}
            self.json_write("calculator.json", addDictionary)
            self.res = res
            self.currentOper = addDictionary
            print(res)
    
    def div(self):
        if self.divTrue:
            res = self.values[0]
            for x in self.values[1: len(self.values)]:
                try:
                    res = res/x
                except ZeroDivisionError:
                    print("Cannot divide!")
                    res = "Error"
                    break
            addDictionary = {"input": self.values,
                             "Operator": "div",
                             "output": res}
            self.json_write("calculator.json", addDictionary)
            self.res = res
            self.currentOper = addDictionary
            print(res)

    def iscommand(self, input):
        if input == "add":
            self.subTrue = False
            self.mulTrue = False
            self.sumTrue = True
            self.divTrue = False
            self.exitTrue = False
        elif input == "sub":
            self.subTrue = True
            self.mulTrue = False
            self.sumTrue = False
            self.divTrue = False
            self.exitTrue = False
        elif input == "mul":
            self.subTrue = False
            self.mulTrue = True
            self.sumTrue = False
            self.divTrue = False
            self.exitTrue = False
        elif input == "div":
            self.subTrue = False
            self.mulTrue = False
            self.sumTrue = False
            self.divTrue = True
            self.exitTrue = False
        elif input == "exit":
            self.subTrue = False
            self.mulTrue = False
            self.sumTrue = False
            self.divTrue = False
            self.exitTrue = True
        return    

""" 
if __name__ == "__main__":
    flag = True
    while flag:
        user_input = input('Enter a operation: ')

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
                flag = not c.exitTrue

     """