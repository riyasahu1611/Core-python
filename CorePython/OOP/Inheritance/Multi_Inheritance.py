class Addition:
    def sum(self,a,b):
        return a+b;

class multiplication:
    def multiply(self,a,b):
        return a*b;

class Divide(Addition, multiplication):
    def Divide(self,a,b):
        return a/b;

Divide_obj = Divide()
print(Divide_obj.sum(10,20))
print(Divide_obj.multiply(50,50))
print(Divide_obj.Divide(60,20))

