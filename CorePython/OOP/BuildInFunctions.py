class Student:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def display_details(self):
        print("name:%s,age:%d"%(self.name, self.age))

s = Student("Riya",25)
# print(Student.__doc__)   #This gives us the class documentation if documentation is present. None otherwise.
# print(Student.__name__) #it will print class name
print(s.__dict__)  #This is a dictionary holding the class namespace.

