'''
Create a class BackAccount with balance,
possibility to deposit some money,
withdrawn and overdraft status (balance < 0).

Any object of that class should have access 
to 4 things: 
- balance (Number)
- overdraft status (Boolean)
- deposit method (Function)
- withdrawn method (Function)
'''


class BankAccount:
    def __init__(self, balance=0, overdraft=False):
        self.balance = balance
        self.overdraft = overdraft

    def deposit(self, money):
        # your code goes here
        pass

    def withdrawn(self, money):
        # your code goes here
        pass



myAccount = BankAccount(100)
print(myAccount.balance)
print(myAccount.overdraft)
