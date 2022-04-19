#combine list of dictionaries `dicts` with the same keys in each list to a single dictionary
.

```
dicts = [{'name': 'John', 'age': 20}, {'name': 'Jane', 'age': 30}, {'name': 'Joe', 'age': 40}]

result = {}
for d in dicts:
    for key, value in d.items():
        result.setdefault(key, []).append(value)

print(result)
```