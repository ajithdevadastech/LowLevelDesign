class Vehicle:
    def startVehicle(self):
        pass

class Car(Vehicle):
    def startVehicle(self):
        print('start the car engine')

class Bicycle(Vehicle):
    def startVehicle(self):
        print('start pedalling')

C = Car()
C.startVehicle()

B = Bicycle()
B.startVehicle()