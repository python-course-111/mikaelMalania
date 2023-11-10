# Classes in python

class Car:
    wheels = 4

    def __init__(self, make, color):
        # Instance attributes
        self.make = make
        self.color = color

    def start_engine(self):
        return f"{self.make} with the color of {self.color} is starting the engine"


# Creating instances of the class
car1 = Car("BMW", "Black")

car2 = Car("Mercedes", "White")

print(car1.make)
print(car2.start_engine())
