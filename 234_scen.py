#find all words in a string `mystring` that start with the `$` sign
.

```
import re

mystring = "This is a string with $ signs in it."

result = re.findall(r"\$\w+", mystring)

print(result)
```