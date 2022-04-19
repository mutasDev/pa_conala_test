#Get a new list `list2`by removing empty list from a list of lists `list1`


```
list1 = [[], [1, 2, 3], [4, 5], [], [], [6, 7, 8], [9], [10, 11, 12], [], [], [13]]
list2 = [i for i in list1 if i]
```