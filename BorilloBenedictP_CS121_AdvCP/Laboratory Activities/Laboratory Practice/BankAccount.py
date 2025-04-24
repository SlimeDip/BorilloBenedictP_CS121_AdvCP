from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def deposit(self, amount):
        pass
            
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type(self):
        pass

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and self._balance - amount >= -5000:
            self._balance -= amount

    def display_account_type(self):
        return "Current Account"

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance.")

    def display_account_type(self):
        return "Savings Account"

def print_account_details(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Type: {account.display_account_type()}")
    print("-" * 40)

acc1 = SavingsAccount("SA123", 1200)
acc2 = CurrentAccount("CA456", 200)

acc1.deposit(500)
acc1.withdraw(300)

acc2.deposit(500)
acc2.withdraw(6000)

print_account_details(acc1)
print_account_details(acc2)