#ex2

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car = Vehicle('nissan', 'leaf', 2015)

print car.make, car.model, car.year
