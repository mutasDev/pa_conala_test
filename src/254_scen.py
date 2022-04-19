#convert a pandas series `sf` into a pandas dataframe `df` with columns `email` and `list`


```
import pandas as pd

sf = pd.Series(['foo@bar.com', 'bar@foo.com'])

df = pd.DataFrame(sf, columns=['email'])

df['list'] = df['email'].apply(lambda x: x.split('@')[0])

print(df)
```