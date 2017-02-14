#ex3


class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print self.make, self.model, self.year



car = Vehicle('nissan', 'leaf', 2015)

car.print_info()
