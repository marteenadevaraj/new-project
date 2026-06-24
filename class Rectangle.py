class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area:", self.l * self.b)

r = Rectangle(5, 4)
r.area()