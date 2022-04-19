#swap keys with values in a dictionary `a`


```
a = {'one': 1, 'two': 2, 'three': 3}

def swap(d):
    return {v: k for k, v in d.items()}

print(swap(a))
```