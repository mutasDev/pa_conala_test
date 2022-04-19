#select values from column 'A' for which corresponding values in column 'B' will be greater than 50, and in column 'C' - equal 900 in dataframe `df`
:

```
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [100, 200, 300, 400, 500], 'C': [900, 800, 700, 600, 500]})

df_new = df.loc[(df['B'] > 50) & (df['C'] == 900)]
```