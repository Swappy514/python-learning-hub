# Introduction to Object Oriented Programming (OOP)

Object Oriented Programming is a paradigm that models real-world entities as objects.

## Key Concepts:

- **Class:** Blueprint for creating objects. It defines attributes and methods.
- **Object/Instance:** An individual instance of a class.
- **Attributes:** Data stored inside an object.
- **Methods:** Functions that belong to a class.

### Example:

class Dog:
def init(self, name, age):
self.name = name
self.age = age
def bark(self):
print(f"{self.name} says Woof!")
my_dog = Dog("Rex", 5)
print(f"My dog's name is {my_dog.name} and age is {my_dog.age}")
my_dog.bark()

### Output:

My dog's name is Rex and age is 5
Rex says Woof!

This allows modeling complex behaviors and organizing code efficiently.
