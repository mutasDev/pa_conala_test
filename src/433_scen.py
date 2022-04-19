#Sum the corresponding decimal values for binary values of each boolean element in list `x`


x = [True, False, True, False]

def sumBinary(x): 

sum = 0

for i in range(len(x)): 

if x[i] == True: 

sum = sum + 1

return sum