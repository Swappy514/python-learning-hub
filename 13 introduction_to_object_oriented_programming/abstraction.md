# Abstraction

Abstraction hides complexity by providing a simpler interface.

Python uses Abstract Base Classes (ABC) to enforce method implementation.

### Example:

from abc import ABC, abstractmethod

class Vehicle(ABC):
@abstractmethod
def start(self):
pass

class Car(Vehicle):
def start(self):
print("Car is starting")

car = Car()
car.start() # Output: Car is starting

Abstraction ensures subclasses implement necessary methods.
