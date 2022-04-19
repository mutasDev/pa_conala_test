#Removing duplicates in list `t`


```
t = [1, 2, 3, 4, 1, 2, 3, 4]

def remove_duplicates(t):
    return list(set(t))

print(remove_duplicates(t))
```