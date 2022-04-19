#remove elements from list `oldlist` that have an index number mentioned in list `removelist`


```
oldlist = [1,2,3,4,5,6,7,8,9,10]
removelist = [2,5,6,7,8,9]

for i in removelist:
    oldlist.pop(i)

print(oldlist)
```