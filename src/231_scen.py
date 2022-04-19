#group a list of dicts `LD` into one dict by key
 `k`

```
LD = [{'k': 'a', 'v': 1}, {'k': 'b', 'v': 2}, {'k': 'a', 'v': 3}]

def group_by_key(LD, k):
    d = {}
    for e in LD:
        if e[k] in d:
            d[e[k]].append(e)
        else:
            d[e[k]] = [e]
    return d
```