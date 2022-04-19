#convert tuple of tuples `(('aa',), ('bb',), ('cc',))` to tuple
 of lists `[['aa'], ['bb'], ['cc']]`

```
tuple_of_lists = [list(tup) for tup in tuple_of_tuples]
```