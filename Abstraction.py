from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def area(self):
        return self.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * self.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length  = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)



o = Circle(6)
print(o.area())
print(o.perimeter())

p = Rectangle(3,4)
print(p.area())
print(p.perimeter())
