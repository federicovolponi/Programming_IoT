class Student():
    def __init__(self, name, surname, birthYear, enroll='bachelor'): 
        self.name=name
        self.surname=surname
        self.birthYear = birthYear
        self.enroll = enroll
        self.bachelor = self.enroll == 'bachelor'
        self.master = self.enroll == 'master'
        self.gradesList = gradesList = []

    def show(self):
        print(f"Hi I'm {self.name} {self.surname}")

    def age(self):
        ####
        studentAge = 2022-int(self.birthYear)
        print(f"{studentAge}")

    def isBachelor(self):
        if self.bachelor == True:
            print("The student is bachelor")
        else:
            print("The student is NOT bachelor")


    def isMaster(self):
        if self.master == True:
            print("The student is master")
        else:
            print("The student is NOT master")

    def saveFile(self):
        f = open('students_list.txt','w')
        toWrite=f"{self.name},{self.surname},{self.birthYear}\n"
        #toWrite= self.name+","+self.surname+","+self.birthYear   #equivalent to the line before
        f.write(toWrite)
        f.close()
    
    def grades(self, filename):
        fileContent = open(filename).read()
        gradesList_str = fileContent.split(",")
        self.gradesList = [int(item) for item in gradesList_str]
        maxGrade = max(self.gradesList)
        minGrade = min(self.gradesList)
        average = sum(self.gradesList)/len(self.gradesList)
        print(f"The student grades are:\nMax: {maxGrade}\nMin: {minGrade}\nAverage: {average}")
    
    def asDictionary(self):
        studentAttributes = {"name": self.name,
                             "surname": self.surname, 
                             "age": 2022-int(self.birthYear), 
                             "grades": self.gradesList }
        print(studentAttributes)
             
#TODO: modify for using json format

# This is the main of our program
if __name__ == "__main__":

    name1=input("Insert your name: ")
    surname1=input("Insert your sourname ")
    Age1 = input("Insert your birthyear ")
    degree =  input("Do you have a bachelor or a master degree? ")
    studentA = Student(name1,surname1, Age1, degree)
    studentA.show()
    studentA.age()
    studentA.saveFile()
    studentA.isBachelor()
    studentA.isMaster()
    studentA.grades("student_grades.txt")
    studentA.asDictionary()