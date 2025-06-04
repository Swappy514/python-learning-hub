# Industry Example: Employee Management System Using OOP

class Employee:
    def __init__(self, name, salary):
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
