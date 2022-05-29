class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance

        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Deposit: ${self.balance}, Interest Rate: {self.int_rate}%")

    def yield_interest(self):
        if self.balance <= 0:
            print("No funds to yeild")
        elif self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
            return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.05, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def accrue_interest(self):
        self.account.yield_interest()
        return self

    def display_Info(self):
        self.account.display_account_info()
        return 
        

user_jes = User("Jesse", "thisemail.com").make_deposit(100).make_withdraw(60).accrue_interest().display_Info()
