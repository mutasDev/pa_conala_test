#check if all elements in list `myList` are identical


```
myList = [1,1,1]

if all(x==myList[0] for x in myList):
    print("All elements in the list are identical")
else:
    print("All elements in the list are not identical")
```