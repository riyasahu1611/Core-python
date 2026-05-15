class Employee:
    def __init__(self, name='', id=0):
        self.name = name
        self.id = id

    # name
    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name

    # id
    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id


class Tester(Employee):
    def __init__(self, specialized=" ", name=" ", id=0):
        self.specialized = specialized
        print("Tester:")
        super().__init__(name, id)

    # specialized
    def set_specialized(self, s):
        self.specialized = s

    def get_specialized(self):
        return self.specialized


class Designer(Employee):
    def __init__(self, type="", specialized =" ", name=" ", id=0):
        self.type = type
        super().__init__(name, id)
        print("\nDesigner:")

    # type
    def set_type(self, t):
        self.type = t

    def get_type(self):
        return self.type

        # Specialized
    def set_specialized(self, t):
        self.specialized = t

    def get_specialized(self):
        return self.type


# Creating Tester object
e = Tester('Testing', 'Ashish Jain', 32)
print("Name:", e.get_name())
print("Employee Id:", e.get_id())
print("Specialized in:", e.get_specialized())

# Creating Designer object
d = Designer('Graphic Designer', "Designing", 'Aman Gupta', 43)
print("Name:", d.get_name())
print("Employee Id:", d.get_id())
print("Specialized in:", d.get_specialized())
print("Type:", d.get_type())
