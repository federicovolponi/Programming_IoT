
class Student():
    def __init__(self, name, surname, Age):
        self.name = name
        self.surname = surname
        self.Age = age
    
    def show(self):
        print(f"hi I'm {self.name} {self.surname}")

    def age(self):
        print(f"I'm {int(self.Age)} years old")


if __name__ == "__main__":
    name = input("Insert your name: ")
    surname = input("Insert yout surname: ")
    age = input("Insert your age: ")

    studentA = Student(name, surname, age)

    studentA.show()
    studentA.age()

   
