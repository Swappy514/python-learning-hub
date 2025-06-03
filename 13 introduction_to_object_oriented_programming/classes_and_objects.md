Classes and Objects
Class: Defines attributes and behaviors.

Object: Instance of a class.

Example:
class Person:
def **init**(self, name, age):
self.name = name
self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

person1 = Person("Alice", 30)
person1.greet()
Output:
Hello, my name is Alice and I'm 30 years old.
This is fundamental OOP building block.
