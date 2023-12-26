"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload
class Plane(Vehicle):
    cargo: int(5)
    max_cargo: int()
    def __init__(self):
        self.max_cargo=10

    def load_cargo(self, load):
        if self.cargo+self.load<=self.max_cargo:
            print(self.cargo+self.load)
        else:
            raise CargoOverload("Cargo_OVERLOAD")

    def remove_all_cargo(self):
        self.cargo=0
        return self.cargo
