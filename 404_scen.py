#converting two lists `[1, 2, 3]` and `[4, 5, 6]` into a matrix


```
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.matrix([a, b])

print(c)
```