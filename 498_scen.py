#sum elements at the same index in list `data`
 and `data2` and stores the result in a new list `result`.

```
data = [1, 2, 3, 4, 5]
data2 = [6, 7, 8, 9, 10]

result = []
for i in range(len(data)):
    result.append(data[i] + data2[i])
```