"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle, NotEnoughFuel, LowFuelError
from engine import Engine


class Car(Vehicle):
    def __init__(self, *args):
        super().__init__()
        self.engine = None


    def set_engine(self, engine: Engine):
        self.engine = engine


# car = Vehicle(weight=158, fuel=0, fuel_consumption=18)
# try:
#     car.start()
#     car.fuel = 0
#     car.start()
#     car.move(10)
# except NotEnoughFuel as e:
#     print(f"Not enough fuel error: {e}")
# except LowFuelError as o:
#     print(f"Low fuel. Cannot start the vehicle: {o}")
