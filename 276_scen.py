#get the position of item `element` in list `testlist`


testlist = [1, 4, 6, 8, 12]

element = int(input("Please enter the element you are looking for: "))

position = testlist.index(element)

print("The position of the element is:", position)