class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print('start the car engine')

class Bicycle(Vehicle):
    def start_engine(self):
        pass #since there is no engine fot bicycle

"""
since bicycle doesn't have engine it can be substituted for Vehicle, which violated Liskov's.
"""

C = Car()
C.start_engine()

B = Bicycle()
B.start_engine()