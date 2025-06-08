# Basics of OOP: Creating Classes and Objects

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def details(self):
        return f"Car: {self.brand} {self.model}"

# Create instances
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.details())
print(car2.details())
