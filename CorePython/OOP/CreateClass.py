class Employee:
    RollNo = 10
    Name = "Riya"

    def display(self):
        print("RollNo:%d\nName:%s"%(self.RollNo, self.Name))

emp = Employee()
emp.display()


class Car:
    Name = "SwiftDzire"
    Color = "Grey"

    def display(self):
        print("Name:%s\nColor:%s"%(self.Name, self.Color))

C = Car()
C.display()