# Multi Level Inheritance using Getter Method

class Animal:

    def __init__(self, name):
        self.__name = name

    # getter method
    def get_name(self):
        return self.__name

    def eat(self):
        print(self.get_name(), "is eating")


class Dog(Animal):

    def bark(self):
        print(self.get_name(), "is barking")


class BabyDog(Dog):

    def weep(self):
        print(self.get_name(), "is weeping")


# object create
b = BabyDog("Tommy")

# methods call
b.eat()
b.bark()
b.weep()
