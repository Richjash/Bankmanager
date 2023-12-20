class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}.New balance : ${self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds,Locked account, Invalid amount")

    def get_balance(self):
        print(f"the account balance  for {self.account_holder}: ${self.balance}")


account1 = BankAccount("Richard Agbadaola")
account1.deposit(1000)
account1.withdraw(500)
account1.get_balance()
