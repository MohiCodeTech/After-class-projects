class Bank_account:
    def __init__(self, balance, amount, owner):
        self.balance = balance
        self.amount = amount
        self.owner = owner
    def withdraw(self, amount):
        self.balance -= amount
        print(f"The amount of {amount} has been withdrawed by {self.owner} remaining balance is {self.balance} ")
    def deposit(self, amount):
        self.balance += amount
        print(f"The amount of {amount} has been deposited by {self.owner} remaining balance is {self.balance} ")
    def __del__(self):
        print("This object has been deleted")

bank1 = Bank_account(10000,2000, "Moheathraam")
bank1.withdraw(2000)
bank1.deposit(3000)