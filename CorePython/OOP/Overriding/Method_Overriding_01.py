class Shape:
    def area(self):
        print("Shape Area...")
        return print("Shape Class Area Method")

class Rectangle(Shape):
    def area(self):
        print("Rectangle Area...")
        return print("Rectangle Class Area Method")

r = Rectangle()
r.area()

r = Shape()
r.area()

Shape: Shape = Rectangle()
Shape.area()

