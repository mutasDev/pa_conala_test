#Check if any key in the dictionary `dict1` starts with the string `EMP$$`


```
dict1 = {'EMP1': 'John', 'EMP2': 'Mike', 'EMP3': 'Tom'}

for key in dict1:
    if key.startswith('EMP$$'):
        print('A key in the dictionary starts with the string "EMP$$".')
        break
else:
    print('No key in the dictionary starts with the string "EMP$$".')
```