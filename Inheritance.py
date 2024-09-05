class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def get_name(self):
        print('The vehicle details are ' + self.name + ' , ' + self.model)

class Fuelcar(Vehicle):
    def __init__(self, name, model, combusttype):
        self.combusttype = combusttype
        Vehicle.__init__(self, name, model)

    def get_fuel_car(self):
        super().get_name()
        print(', ' + self.combusttype)

class Electriccar(Vehicle):
    def __init__(self, name, model, batterypower):
        self.batterypower = batterypower
        Vehicle.__init__(self, name, model)

    def get_electric_car(self):
        super().get_name()
        print(', ' + self.batterypower)

class Gasolinecar(Fuelcar):
    def __init__(self, name, model, combusttype, gascapacity):
        self.gascapacity = gascapacity
        Fuelcar.__init__(self, name, model, combusttype)

    def get_gasoline_car(self):
        super().get_fuel_car()
        print(', ' + self.gascapacity)

class Hybridcar(Gasolinecar, Electriccar):
    def __init__(self, name, model, combusttype, gascapacity, batterypower):
        self.batterypower = batterypower
        Gasolinecar.__init__(self, name, model, combusttype, gascapacity)

    def get_hybrid_car(self):
        super().get_gasoline_car()
        print(', ' + self.batterypower)

o = Vehicle('Tesla', 'Model Y')
o.get_name()

p = Fuelcar('Honda', 'CRV', '4 cyl')
p.get_fuel_car()

q = Electriccar('Tesla', 'Model Y', '200W')
q.get_electric_car()

r = Gasolinecar('Honda', 'CRV', '4 cyl', '12L')
r.get_gasoline_car()

s = Hybridcar('Honda', 'CRV', '4 cyl', '12L', '300W')
s.get_hybrid_car()



