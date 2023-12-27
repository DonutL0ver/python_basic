"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload
class Plane(Vehicle):
    def __init__(self, *args):
        super().__init__()
        self.max_cargo=10
        self.cargo=int(5)

    def load_cargo(self, load):
        if self.cargo+load<=self.max_cargo :
            self.cargo+int(load)
        else:
            raise CargoOverload("Cargo_OVERLOAD")

    def remove_all_cargo(self):
        self.cargo=0
        return self.cargo

plane = Plane()
try:
    plane.load_cargo(10)
except CargoOverload as e:
    print(f"Not enough fuel error: {e}")