class person:
    count = 0
    avg_age = 18

    def __init__(self):
        self.__name = ''
        self.__address = ''
        self.__age = ''
        # person.count += 1
#name
    def get_name(self):
        return self.__name

    def set_name(self, n):
        self.__name = n
#address
    def get_address(self):
        return self.__address

    def set_address(self, a):
        self.__address = a
#age
    def get_age(self):
       return self.__age

    def set_age(self, A):
        self.__age = A

p = person()
p.set_name("Riya Sahu")
p.set_address("Indore")
p.set_age('25')
print("Name:", p.get_name())
print("Address:", p.get_address())
print("Age:", p.get_age())
