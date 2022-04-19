#reverse sort counter `x` by value


```
import collections

x = collections.Counter({'a': 4, 'b': 2, 'c': 3, 'd': 1})

for key, value in sorted(x.items(), key=lambda kv: kv[1], reverse=True):
    print("%s: %s" % (key, value))
```