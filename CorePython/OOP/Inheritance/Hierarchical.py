class Shape:
    def __init__(self, color='', border_width = 0):
        self.color = color
        self.border_width = border_width
#color
    def set_color(self, c):
        self.color = c

    def get_color(self):
        return self.color

#Border_width
    def set_border_width(self, bw):
        self.border_width = bw

    def get_border_width(self):
        return self.border_width

class Rectangle(Shape):
    def __init__(self, length= 0, width = 0, color='', border_width= 0):
        self.length = length
        self.width = width
        print("Rectangle:")
        super().__init__(color, border_width)

#length
    def set_length(self, l):
        self.length = l

    def get_length(self):
        return self.length

#width
    def set_width(self, w):
        self.width = w

    def get_width(self):
        return self.width

class Circle(Shape):
        def __init__(self, radius = 0, color='', border_width=0):
            self.radius = radius
            super().__init__(color, border_width)
            print("\nCircle:")

#radius
        def set_radius(self, r):
            self.radius = r

        def get_radius(self):
            return self.radius

# Creating a Rectangle object
r = Rectangle(10, 20, "Red", 200)
print("Length:", r.get_length())
print("Width:", r.get_width())
print("Color:", r.get_color())
print("Border Width:", r.get_border_width())

# Creating a Circle object
c = Circle(25,"Green", 300 )
print("Radius:", c.get_radius())
print("Color:", c.get_color())
print("Border Width:", c.get_border_width())
