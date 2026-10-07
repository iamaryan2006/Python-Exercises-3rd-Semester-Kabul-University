from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, account_num, balance=0):
        self.account_num = account_num
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self._balance

    @abstractmethod
    def calculate_fee_or_benefit(self):
        pass

    def __str__(self):
        return f"Account {self.account_num}: Balance = ${self._balance}"


class SavingsAccount(Account):

    def calculate_fee_or_benefit(self):
        return self._balance * 0.05


class CurrentAccount(Account):

    def calculate_fee_or_benefit(self):
        return 10


savings = SavingsAccount("SA001", 1000)
current = CurrentAccount("CA001", 1000)

savings.deposit(500)
savings.withdraw(200)

current.deposit(300)
current.withdraw(100)

accounts = [savings, current]

for account in accounts:
    print(account)
    print("Fee/Benefit:", account.calculate_fee_or_benefit())
    print()