#get a dictionary `records` of key-value pairs in PyMongo cursor `cursor`
 and converts it to a list of dictionaries.

```
records = []
for record in cursor:
    records.append(record)
```