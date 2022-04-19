#create a list containing each two adjacent letters in string `word` as its elements
.

```
word = "hello"

lst = []

for i in range(len(word)-1):
    lst.append(word[i:i+2])
    
print(lst)
```