from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel, CargoOverload


class Vehicle(LowFuelError, NotEnoughFuel, CargoOverload, ABC):
    def __init__(self, weight=200, fuel=0, fuel_consumption=15):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        try:
            if self.fuel == 0:
                self.started = False
                raise LowFuelError('Low fuel. Cannot start the vehicle', self.fuel)
            elif not self.started and self.fuel > 0:
                self.started = True
                print("STARTED")
            elif self.started and self.fuel == 0:
                self.started = False
                raise LowFuelError('Low fuel. Cannot start the vehicle', self.fuel)
            else:
                pass
        except LowFuelError as error:
            print(error)



    def move(self, distance):
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
