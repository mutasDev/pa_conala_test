#regex, find "n"s only in the middle of string `s`


import re

s = "The quick brown fox jumps over the lazy dog"

result = re.findall(r"\bn\b", s)

print(result)