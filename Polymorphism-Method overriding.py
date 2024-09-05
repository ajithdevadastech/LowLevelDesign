class Animal:
    def __init__(self):
        pass
    def makesound(self):
        print('The animal makes sound.')

    def eat(self):
        print('The animal eats plants and meat.')

class Lion(Animal):
    def __init__(self):
        pass
    def makesound(self):
        print('The lion roars.')

o = Lion()
o.makesound()
o.eat()
