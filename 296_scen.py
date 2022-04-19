#unzip list `[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', )]` and fill empty results with None


```
unzipped = list(zip(*[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', )]))
unzipped[1] = [x if x is not None else None for x in unzipped[1]]
```