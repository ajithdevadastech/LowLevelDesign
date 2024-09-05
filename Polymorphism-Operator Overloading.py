class complex:
    def __init__(self):
        self.real = 0
        self.imaginary = 0

    def setvalue(self, i, j):
        self.real = i
        self.imaginary = j

    def __add__(self, c):
        result = complex()
        result.real = self.real + c.real
        result.imaginary = self.imaginary + c.imaginary
        return result

    def display(self):
        print (str(self.real) + ' + ' + str(self.imaginary) + 'j' )

c1 = complex()
c1.setvalue(2, 3)

c2 = complex()
c2.setvalue(5, 6)

r = c1 + c2
r.display()
