#Split string `input` at every space followed by an upper-case letter
.

```
def split_at_uppercase(input):
  return re.findall('[A-Z][^A-Z]*', input)
```