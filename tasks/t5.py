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
<<<<<<< HEAD
        self.balance += money
        self.overdraft_balance()
        print(self.balance)
        

    def withdrawn(self, money):
        self.balance -= money
        self.overdraft_balance()

    def overdraft_balance(self):
        if self.balance < 0 :
            self.overdraft = True
    


myAccount = BankAccount(100)
myAccount.withdrawn(101)
=======
        # your code goes here
        pass

    def withdrawn(self, money):
        # your code goes here
        pass



myAccount = BankAccount(100)
>>>>>>> 3e019487c0191bf5e4cada8962afcca6683761bb
print(myAccount.balance)
print(myAccount.overdraft)
