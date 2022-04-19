#write the data of dataframe `df` into text file `np.txt`


```
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

df.to_csv('np.txt', index=False)
```