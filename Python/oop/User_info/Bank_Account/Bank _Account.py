
balance = 0
int_rate = 0.03

class BankAccount:
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, dep):
        self.balance = self.balance + dep
        print(f"Available balance ${self.balance}")
        return self

    def withdraw(self, withdraw):
        if self.balance > withdraw:
            self.balance = self.balance - withdraw
            print(f"Amount to be withdrawn ${withdraw}")
            print(f"Available balance ${self.balance}")
        else:
            self.balance = self.balance -5
            print(f"Available balance ${self.balance}")
            print(f"Withdraw amount ${withdraw} Insuffiecient funds. A charge of $5.00 has been applied")
            print(f"Avaialbe balance ${self.balance}")
        return self

    def account_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Available funds: ${self.balance}")
        print(f"Interest rate: {self.int_rate}")
        return self

    def yield_interest(self):
        self.balance = self.balance * (1 + int_rate)
        print(self.balance)
        return self

user_1 = BankAccount("Mike", "Start", 0)
user_2 = BankAccount("Gary", "Bary", 0)


user_1.deposit(500).deposit(35).deposit(450).withdraw(300).yield_interest().account_info()
user_2.deposit(250).deposit(300).withdraw(150).withdraw(350).withdraw(35).withdraw(200).yield_interest().account_info()

