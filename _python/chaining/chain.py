class User:
    def __init__(self, first_name, last_name, account):
        self.first_name = first_name
        self.last_name = last_name
        self.account = account

    def deposit(self, amount):
        self.account += amount
        return self

    def withdraw(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print("User : {} {}, Balance: {}" .format(
            self.first_name, self.last_name, self.account))
        return self

    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount
        return self


manar = User("Manar", "Hasan", 400)
mohammad = User("Mohammad", "Husseini", 700)
salah = User("Salah", "AbuKarsh", 100)
manar.deposit(100).deposit(100).deposit(
    100).withdraw(100).display_user_balance()
mohammad.deposit(200).deposit(300).withdraw(
    500).withdraw(50).display_user_balance()
salah.deposit(20).withdraw(10).withdraw(5).withdraw(10).display_user_balance()
manar.transfer_money(salah, 200).display_user_balance()
salah.display_user_balance()
