# Industry Example: Employee Management System Using OOP

This example demonstrates:

- A base class `Employee` with a `work` method.
- Derived classes `Manager` and `Developer` overriding `work`.
- Polymorphism: The same method name behaves differently depending on the object.

### Code:

class Employee:
def init(self, name, salary):
self.name = name
self.salary = salary
def work(self):
print(f"{self.name} is working.")
class Manager(Employee):
def work(self):
print(f"{self.name} is managing the team.")

class Developer(Employee):
def work(self):
print(f"{self.name} is writing code.")

employees = [
Manager("Alice", 80000),
Developer("Bob", 60000),
Developer("Charlie", 65000)
]

for emp in employees:
emp.work()

### Output:

Alice is managing the team.
Bob is writing code.
Charlie is writing code.

This structure supports scalable and maintainable software design.
