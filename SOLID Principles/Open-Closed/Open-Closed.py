from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def CalculateArea(self):
        pass

    @abstractmethod
    def CalculatePerimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def CalculateArea(self):
        return self.length * self.breadth

    def CalculatePerimeter(self):
        return 2 * (self.length + self.breadth)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def CalculateArea(self):
        return 3.14 * self.radius ** 2

    def CalculatePerimeter(self):
        return 2 * 3.14 * self.radius


R = Rectangle(10,20)
print(R.CalculateArea())
print (R.CalculatePerimeter())

C = Circle(10)
print(C.CalculateArea())
print(C.CalculatePerimeter())

"""
for Triangle, another class can be created. The base class is not modified but only extended here.
"""
