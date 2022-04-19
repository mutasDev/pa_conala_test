#get elements from list `myList`, that have a field `n` value 30


myList = [{'n': 10}, {'n': 20}, {'n': 30}, {'n': 40}]

for element in myList:
    if element['n'] == 30:
        print(element)