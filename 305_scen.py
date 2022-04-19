#filter dataframe `df` by values in column `A` that appear more than once
.

```
df = df[df['A'].duplicated(keep=False)]
```