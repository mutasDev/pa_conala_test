#check if a pandas dataframe `df`'s index is sorted


```
if df.index.is_monotonic:
    print("Index is sorted")
else:
    print("Index is not sorted")
```