#unzip the list `[('a', 1), ('b', 2), ('c', 3), ('d', 4)]`


```
unzipped = zip(*[('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# the * operator unpacks a list into positional arguments
a, b, c, d = unzipped
```