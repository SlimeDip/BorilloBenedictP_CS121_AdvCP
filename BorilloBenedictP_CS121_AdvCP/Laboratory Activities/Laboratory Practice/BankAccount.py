from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self):
        self._account_number = ""
        self._balance = 0

    @property
    def account_number(self):
        return self._account_number
    
    @account_number.setter
    def account_number(self, get_account_number):
        self._account_number = get_account_number

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, add_balance):
        if add_balance > 0:
            self._balance = add_balance
        else:
            self._balance = 0

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

acc1 = SavingsAccount()
acc2 = CurrentAccount()

acc1.account_number = "SA123"
acc2.account_number = "CA456"

acc1.balance = 0
acc2.balance = 0

acc1.deposit(1500)
acc1.withdraw(300)

acc2.deposit(700)
acc2.withdraw(900)

print_account_details(acc1)
print_account_details(acc2)
