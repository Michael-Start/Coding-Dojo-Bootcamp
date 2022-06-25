
balance = 0
int_rate = 0.03

class BankAccount:
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate

    def make_deposit(self, dep):
        self.balance += dep
        print(f"Account balance: {self.balance}")
        return self
    
    def make_withdraw(self, withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
            print(f"Amount to be withdrawn ${withdraw}")
            print(f"Available balance ${self.balance}")
        else:
            self.balance -=5
            print(f"Available balance ${self.balance}")
            print(f"Withdraw amount ${withdraw} Insufficient funds. A charge of $5.00 has been applied")
            print(f"Available balance ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance * (1 + int_rate)
        print(self.balance)
        return self

class User:
    population = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account = BankAccount(balance, int_rate)
        User.population +=1

    def account_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email Address: {self.email}")
        print(f"Account Balance: {self.account.balance}")
        print(f"Interest Rate: {self.account.int_rate}")

    def deposit(self, amount_deposit):
        self.account.make_deposit(amount_deposit)
        return self

    def withdraw(self, amount_withdraw):
        self.account.make_withdraw(amount_withdraw)
        return self



user1 = User("Mike", "Start", "address@email.com")
user2 = User("Gary", "Bary", "email@address.com")

user1.account_info()
user1.deposit(500).withdraw(200)

user1.account_info()
