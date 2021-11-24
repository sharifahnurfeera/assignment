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
        
p1 = Account("John", 10)  
p2 = Account("Ani", 11)  
p3 = Account("Abu", 12)  

#Do some transactions
print(p1.__str__())
p1.deposit(2)
print(p1)
p1.withdraw(5)
print(str(p1))

p2.deposit(2)
p2.withdraw(5)

p3.deposit(2)
p3.withdraw(5)

# creating list       
list = [] 

# appending instances to list 
list.append(p1)
list.append(p2)
list.append(p3)

for obj in list:
    print( obj.name, obj.balance )

accountTuple = tuple(())
accountTuple = tuple(list)

for x in accountTuple:
  print(x)


"""
Explanation/ thought process

When to use a Tuple:
— When you know you will not modify or change after creation.
— Your content is sorted or has a structure for retrieval.
When to use a Dictionary:
— When your data does’t have a structure and quick retrieval is the primary concern.
— Space complexity is not a concern.
When to use a List:
— When you are unsure whether your data structure will grow.
— Best choice to use when experimenting ( great size / retrieval speed trade-off).
"""
