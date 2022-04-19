#count the occurrences of items in list `l`


```
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counts = {}

for item in l:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print(counts)
```