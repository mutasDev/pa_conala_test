#get an array of the mean of each two consecutive values in numpy array `x`


```
import numpy as np

def mean_of_two_consecutive(x):
  return np.mean(x[1:], x[:-1])
```