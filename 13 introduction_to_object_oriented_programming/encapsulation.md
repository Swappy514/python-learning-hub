# Encapsulation

Encapsulation hides internal state and requires all interaction to be performed through an object's methods.

- Prefixing attributes with `__` makes them private.
- Access is provided through public methods (getters/setters).

### Example:

class Account:
def init(self, owner, balance):
self.owner = owner
self.**balance = balance # private
def deposit(self, amount):
if amount > 0:
self.**balance += amount

def get_balance(self):
return self.\_\_balance
acc = Account("John", 1000)
acc.deposit(500)
print(acc.get_balance()) # 1500

This protects data integrity.
