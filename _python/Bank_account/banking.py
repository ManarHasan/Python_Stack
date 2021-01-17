class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance <= 0:
            print("You have insufficient funds")
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance <= 0:
            print("You have insufficient funds")
        self.balance += self.balance * self.int_rate
        return self


manar = BankAccount(0.02, 500)
moh = BankAccount(0.01, 500)
manar.deposit(100).deposit(100).deposit(100).withdraw(
    300).yield_interest().display_account_info()
moh.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(
    50).withdraw(50).yield_interest().display_account_info()
