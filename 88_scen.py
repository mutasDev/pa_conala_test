#convert a list of lists `L` to list of integers
.

```
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list = []
for sublist in L:
    for item in sublist:
        new_list.append(int(item))
```