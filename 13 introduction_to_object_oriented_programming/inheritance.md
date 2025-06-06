# Inheritance

Inheritance allows one class to inherit attributes and methods from another.

### Example:

class Animal:
def init(self, name):
self.name = name
def speak(self):
print(f"{self.name} makes a sound.")
class Dog(Animal):
def speak(self):
print(f"{self.name} says woof!")

dog = Dog("Buddy")
dog.speak() # Output: Buddy says woof!

Inheritance promotes code reuse and polymorphism.
