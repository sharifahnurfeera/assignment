x = 1
for i in range(100,0,-1):
    #print(i, end="")
    #print('')
    #print(i)
    x *= i
    #print(x)
    #break
      
#print("Finally")
#print(str(x))

y = 0
#print("Then")
for j in str(x):
  #print(j) 
  y += int(j)
  #print(y)


print("The sum of the digits in the number 100! is:")
print(str(y))  
