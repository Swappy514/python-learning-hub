# Abstraction Example: Using Abstract Base Classes

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")

car = Car()
bike = Bike()

car.start()
bike.start()
