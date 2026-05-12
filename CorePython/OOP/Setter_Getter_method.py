#Setter method
#
class student:

    def set_name(self,name,age,address,city):
        self.name = name
        self.age = age
        self.address = address
        self.city = city

s1 = student()
s1.set_name("Riya", 25, "Tilak Nagar", "Indore")
print("Student name:",s1.name,"\nHer age:",s1.age, "\nadrress:",s1.address, "\ncity:", s1.city)


# Getter Method
#
class student:

    def set_name(self, name,age,address,city):
        self.name = name
        self.age = age
        self.address = address
        self.city = city

    def get_name(self):
        return self.city

s1 = student()
s1.set_name("Riya", 25, "Tilak Nagar","Indore")
print(s1.get_name())

