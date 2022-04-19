#finding the index of elements containing substring 'how' and 'what' in a list of strings 'myList'.


myList = ['how', 'are', 'you', 'what', 'is', 'your', 'name']

for i in range(len(myList)):
    if 'how' in myList[i] or 'what' in myList[i]:
        print(i)