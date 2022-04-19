#reverse the keys and values in a dictionary `myDictionary`


```
myDictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

reversedDictionary = dict(zip(myDictionary.values(), myDictionary.keys()))

print(reversedDictionary)
```