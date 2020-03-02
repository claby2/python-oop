### [1] Construting a class

class Student(): 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self): 
        print("Hello my name is " + self.name)
    
    def old(self):
        print("My age is " + self.age)


username = input("Input Name:\n")
userage = input("Input Age:\n")

user = Student(username, userage)

user.greet()
user.old()

# The __init__ function assigns values to object properties
# Remember! The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


### [2] Storing and iterating through objects

students = []

for i in range(20):
    user = Student("username", "15")
    students.append(user)

for student in students:
    student.greet()