class User:
    def __init__(self, first_name, last_name, account):
        self.first_name = first_name
        self.last_name = last_name
        self.account = account

    def deposit(self, amount):
        self.account += amount

    def withdraw(self, amount):
        self.account -= amount

    def display_user_balance(self):
        print("User : {} {}, Balance: {}" .format(
            self.first_name, self.last_name, self.account))

    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount


manar = User("Manar", "Hasan", 400)
mohammad = User("Mohammad", "Husseini", 700)
salah = User("Salah", "AbuKarsh", 100)
manar.deposit(100)
manar.deposit(100)
manar.deposit(100)
manar.withdraw(100)
manar.display_user_balance()
mohammad.deposit(200)
mohammad.deposit(300)
mohammad.withdraw(500)
mohammad.withdraw(50)
mohammad.display_user_balance()
salah.deposit(20)
salah.withdraw(10)
salah.withdraw(5)
salah.withdraw(10)
salah.display_user_balance()
manar.transfer_money(salah, 200)
manar.display_user_balance()
salah.display_user_balance()
