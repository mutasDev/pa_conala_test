#unzip list `[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', )]`


```
unzipped = list(zip(*[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', )]))
print(unzipped)
```