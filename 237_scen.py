#calculate mean across dimension in a 2d array `a`


```
import numpy as np

a = np.array([[1,2,3], [4,5,6]])

mean_a = a.mean(axis=1)

print(mean_a)
```