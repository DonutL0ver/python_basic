from abc import ABC, abstractmethod
from exeptions.exceptions import CargoOverload,LowFuelError,NotEnoughFuel

class Vehicle(ABC):

    def __init__(self, weight=200, fuel=0, fuel_consumption=15):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    @abstractmethod
    def start(self):
        pass

    def move(self, distance):
        if self.started:
            if self.fuel >= self.fuel_consumption * distance:
                self.fuel -= self.fuel_consumption * distance
                print(f"Moved {distance} km")
            else:
                raise NotEnoughFuel("Not enough fuel to cover the distance", self.fuel_consumption)
        else:
            print("Vehicle is not started")


class Car(Vehicle):
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


class Child(Car):
    def my_method(self):
        print('Вызов метода наследника')
