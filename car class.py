class Car:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Car:", self.name)

c = Car("BMW")
c.show()