#Get a list of pairs from a string `word` using lambda function


```
word = "abcdef"

pairs = lambda word: [(word[i], word[i+1]) for i in range(0, len(word), 2)]

print(pairs(word))
```