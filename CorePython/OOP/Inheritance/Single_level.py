class Shape:
    def __init__(self):
        self.color = ''
        self.border_width = 0
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
    def __init__(self):
        self.length = 0
        self.width = 0
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

r = Rectangle()
r.set_length(30)
r.set_width(20)
r.set_color("Black")
r.set_border_width(200)

print("length:", r.get_length())
print("width:", r.get_width())
print("color:", r.get_color())
print("border_width:", r.get_border_width())
