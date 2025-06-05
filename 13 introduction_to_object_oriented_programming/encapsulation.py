# Encapsulation: Hiding internal data

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def get_balance(self):
        return self.__balance

acc = Account("John", 1000)
acc.deposit(500)
print(f"Balance: {acc.get_balance()}")

# Trying to access private attribute directly will raise error
# print(acc.__balance)  # AttributeError: 'Account' object has no attribute '__balance'
