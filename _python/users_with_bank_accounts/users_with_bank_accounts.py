class User:
    def __init__(self, name, email, balance, int_rate, account_name):
        self.name = name
        self.email = email
        self.account_name = account_name
        self.account_name = BankAccount(int_rate, balance=balance)


class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance = self.balance * self.int_rate
        return self


manar = User("Manar", "manar@axsos.me", 500, 0.02, "mino")
manar.account_name.deposit(120)
manar.account_name.withdraw(150)
manar.account_name.display_account_info()
