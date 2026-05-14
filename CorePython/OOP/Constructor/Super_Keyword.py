class Shape:
    def __init__(self,color, border_width):
        self.color = color
        self.border_width = border_width

    # color
    def set_color(self, c):
        self.color = c

    def get_color(self):
        return self.color

    # Border_width
    def set_border_width(self, bw):
        self.border_width = bw

    def get_border_width(self):
        return self.border_width


class Rectangle(Shape):
    def __init__(self, length=0, width=0, color=' ', border_width=0):
        self.length = length
        self.width = width
        super().__init__(color, border_width)

    # length
    def set_length(self, l):
        self.length = l

    def get_length(self):
        return self.length

    # width
    def set_width(self, w):
        self.width = w

    def get_width(self):
        return self.width


r = Rectangle(10, 20, 'Blue', 200)
print("Rectangle specialization given below:")
print("length:", r.get_length())
print("width:", r.get_width())
print("color:", r.get_color())
print("border_width:", r.get_border_width())
