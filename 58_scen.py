#Merge a nested dictionary `dicts` into a flat dictionary by concatenating nested values with the same key `k`
 into a list.

```
def merge_dicts(dicts):
    merged = {}
    for d in dicts:
        for k, v in d.items():
            if k in merged:
                merged[k].append(v)
            else:
                merged[k] = [v]
    return merged
```