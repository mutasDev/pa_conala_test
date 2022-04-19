#find intersection data between series `s1` and series `s2`


```
import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([4, 5, 6, 7, 8])

s1_s2_intersect = s1.intersect(s2)

print(s1_s2_intersect)
```