"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, message, fuel):
        super().__init__(message)
        self.fuel = fuel


class NotEnoughFuel(Exception):
    def __init__(self, message, fuel_consumption):
        super().__init__(message)
        self.fuel_consumption = fuel_consumption


class CargoOverload(Exception):
    pass