#Find octal characters matches from a string `str` using regex


import re

str = "This is an example string"

result = re.findall(r'[0-7]', str)

print(result)