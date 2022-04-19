#create list of values from dictionary `dict1` that have a key that starts with 'EMP$$'


```
dict1 = {'EMP001': 'John', 'EMP002': 'Mike', 'EMP003': 'Tom', 'EMP004': 'Mary'}

list1 = []
for key in dict1:
    if key.startswith('EMP$$'):
        list1.append(dict1[key])

print(list1)
```