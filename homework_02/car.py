"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle,NotEnoughFuel
from engine import Engine
class Car(Vehicle):
    def __init__(self, weight=200, fuel=100, fuel_consumption=5):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine=None

    def set_engine(self,engine:Engine):
        self.engine=engine
car = Vehicle()
car.start()
try:
    car.move(10)
except NotEnoughFuel as e:
    print(f"Not enough fuel error: {e}")
