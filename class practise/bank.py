#Create a class to represent a bank account. This class 
#should have methods for withdrawing and depositing funds,
# as well as checking the account balance.

class Bank_acc:
    def __init__(self,start_money):
        self.balance=start_money

    def deposit(self,money):
        self.balance+=money
    
    def withdraw(self,money):
        if(money>self.balance):
            print("You need more money to withdraw that much")
        else:
            self.balance-=money
    def check(self):
        print(f"Current account balance: {self.balance}")

x=Bank_acc(1000)
x.deposit(300)
x.withdraw(400)
x.check()