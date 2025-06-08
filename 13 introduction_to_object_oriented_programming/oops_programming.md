# OOP Programming Basics

Classes are templates for objects. Creating an object from a class is called instantiation.

### Example:

class Car:
def init(self, brand, model):
self.brand = brand
self.model = model
def details(self):
return f"Car: {self.brand} {self.model}"
car1 = Car("Toyota", "Corolla")
print(car1.details()) # Output: Car: Toyota Corolla
You can create multiple objects with different attribute values.
