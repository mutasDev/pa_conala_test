#Get a list of integers `lst` from a file `filename.txt`
 and prints the sum of the integers in the list.

```
with open('filename.txt') as f:
    lst = [int(x) for x in f.read().split()]

print(sum(lst))
```