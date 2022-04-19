#filter rows containing key word `ball` in column `ids`


```
import pandas as pd

df = pd.read_csv('data.csv')

df = df[df['ids'].str.contains('ball')]
```