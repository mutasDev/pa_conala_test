#sort a list of dictionary `list` first by key `points` and then by `time`


```
list.sort(key=lambda x: (x['points'], x['time']))
```