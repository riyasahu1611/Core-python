class Student:
    def getStudent(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")

class Test(Student):
    def getMarks(self):
        self.studentclass = input("Class: ")
        print("Enter the marks of respective subjects")
        self.maths = int(input("Maths: "))
        self.english = int(input("English: "))
        self.physics = int(input("Physics: "))
        self.biology = int(input("Biology: "))

class Marks(Test):           #Display student's information along with total marks
    def display(self):
        print("\nName: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("studentclass: ",self.studentclass)
        print("Maths: ",self.maths)
        print("English: ",self.english)
        print("Physics: ",self.physics)
        print("Biology: ",self.biology)

# Create an object of Marks class
m = Marks()
#
# # Collect student details
m.getStudent()
#
# # Collect marks details
m.getMarks()
#
# # Display all information
m.display()






