#pandas: delete rows in dataframe `df` based on multiple columns values


```
df = df.drop(df[(df['column1'] == value1) & (df['column2'] == value2)].index)
```