#calculate the mean of each element in array `x` with the element previous to it
.

```
x = [1, 2, 3, 4, 5]

mean = []

for i in range(1, len(x)):
    mean.append((x[i] + x[i-1]) / 2.0)

print(mean)
```