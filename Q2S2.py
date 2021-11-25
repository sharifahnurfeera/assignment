class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
    	self.balance += amount

    def withdraw(self, amount):
    	self.balance -= amount

    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"
    
class AccountDev(Account):
    def __init__(self, name, balance, accountno):
      super().__init__(name, balance)
      self.accountno = accountno
      
	# getter method
    def get_balance(self):
        return self.balance
      
    # setter method
    def set_balance(self, x):
        self.balance = x
        
    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}. Account Number: {self.accountno}"
        
    def transfer( self, acc2, amount):
    	#print(str(acc1)) 
        #print(str(acc2))
        #print("Transfer 10 from john to puteri")
        #get balance from puteri's acc
        print("")
        print("amount transferred is:")
        print(amount)
        x = self.get_balance()
        y = x - amount
        self.set_balance(y)
        print("")
        print("account transferred from balance is:")
        print(y)
        #get john's balance
        i = acc2.get_balance()         
        #perform deposit 
        j = i + amount
        acc2.set_balance(j)
        print("")
        print("account transferred to balance is:")
        print(j)
        print("")
        #print(str(acc1))        
        #print(str(acc2))
        
        
acc1 = AccountDev("John", 400, 123456789) 
acc2 = AccountDev("Puteri", 250, 123456790) 
print("")
print("Transfer from John's account to Puteri's account")
print("before transfer")
print(str(acc1))        
print(str(acc2))
acc1.transfer(acc2, 10)
print("after transfer")
print(str(acc1))        
print(str(acc2))
print("")
print("Transfer from Puteri's account to John's account")
print("before transfer")
print(str(acc1))        
print(str(acc2))
acc2.transfer(acc1, 20)
print("after transfer")
print(str(acc1))        
print(str(acc2))


