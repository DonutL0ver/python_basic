from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel, CargoOverload
class Vehicle(LowFuelError, NotEnoughFuel, CargoOverload,ABC):
    def __init__(self, weight=200, fuel=600, fuel_consumption=15):
        self.weight=weight
        self.fuel=fuel
        self.fuel_consumption=fuel_consumption
        self.started = False
    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print("Vehicle started")
            else:
                raise LowFuelError("Low fuel. Cannot start the vehicle", self.fuel)
        else:
            print("Vehicle is already started")

    def move(self,distance):
        if self.started:
            if self.fuel >= self.fuel_consumption * distance:
                self.fuel -= self.fuel_consumption * distance
                print(f"Moved {distance} km")
            else:
                raise NotEnoughFuel("Not enough fuel to cover the distance", self.fuel_consumption)
        else:
            print("Vehicle is not started")

    class LowFuelError(Exception):
        def init(self, message, fuel):
            self.fuel = fuel

    class NotEnoughFuel(Exception):
        def init(self, message, fuel_consumption):
            self.fuel_consumption = fuel_consumption

class Child(Vehicle):  # объявите класс наследник
    def my_method(self):
        print('Вызов метода наследника')
