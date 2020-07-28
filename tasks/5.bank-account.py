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

    # your code goes here


myAccount = BankAccount(100)
print(myAccount.balance)
print(myAccount.overdraft)
