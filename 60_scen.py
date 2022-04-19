#identify duplicate values in list `mylist`


```
mylist = [1,2,2,3,3,4,5]

duplicates = []

for i in range(len(mylist)):
    for j in range(i+1, len(mylist)):
        if mylist[i] == mylist[j]:
            duplicates.append(mylist[i])

print(duplicates)
```