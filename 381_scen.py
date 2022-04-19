#numpy concatenate two arrays `a` and `b` along the second axis
.

```
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

c = np.concatenate((a, b), axis=1)

print(c)
```