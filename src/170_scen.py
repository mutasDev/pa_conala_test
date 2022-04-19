#select rows in a dataframe `df` column 'closing_price' between two values 99 and 101


```
df.loc[(df['closing_price'] > 99) & (df['closing_price'] < 101)]
```