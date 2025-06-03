# Classes and Objects: Detailed Example with Methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Create object and call method
person1 = Person("Alice", 30)
person1.greet()
