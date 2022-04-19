#generate all 2-element subsets of tuple `(1, 2, 3)`


```
for i in range(3):
    for j in range(i+1, 3):
        print((1, 2, 3)[i], (1, 2, 3)[j])
```