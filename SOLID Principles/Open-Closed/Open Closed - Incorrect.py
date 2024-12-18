class ShapeCalculator:
    def __init__(self, shape=None, length=0, breadth=0, radius=0):
        self.shape =  shape
        self.length = length
        self.breadth = breadth
        self.radius = radius

    def CalculateArea(self):
        if self.shape == 'Rectangle':
            return self.length * self.breadth
        if self.shape == 'Circle':
            return 3.14 * self.radius * self.radius

    def CalculatePerimeter(self):
        if self.shape == 'Rectangle':
            return 2 * (self.length + self.breadth)
        if self.shape == 'Circle':
            return 2 * 3.14 * self.radius

SC1 = ShapeCalculator('Rectangle', 5, 10)
print(SC1.CalculateArea())
print (SC1.CalculatePerimeter())

SC2 = ShapeCalculator('Circle', radius=5)
print(SC2.CalculateArea())
print (SC2.CalculatePerimeter())

"""
now, to include the logic for Triangle, we need to change the constructor and the methods.
This is modification of the class and is not a good practice.
Violates Open Closed principle.
"""