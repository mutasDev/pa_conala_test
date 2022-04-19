#find the string in `your_string` between two special characters "[" and "]"


```
your_string = "This is [my string]"

result = your_string.split("[")[1].split("]")[0]

print(result)
```