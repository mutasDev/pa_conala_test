#get the highest element in absolute value in a numpy matrix `x`


```
import numpy as np

x = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

abs_max = np.max(np.abs(x))

print(abs_max)
```