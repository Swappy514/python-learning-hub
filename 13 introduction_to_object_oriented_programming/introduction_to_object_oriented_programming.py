# Introduction to Object Oriented Programming (OOP) in Python

# OOP organizes code into objects containing both data and functions.

# Example: Define a simple class and create an object

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Create an object (instance) of Dog
my_dog = Dog("Rex", 5)

# Access attributes and methods
print(f"My dog's name is {my_dog.name} and age is {my_dog.age}")
my_dog.bark()
