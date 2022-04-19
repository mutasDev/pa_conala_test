#Remove duplicate words from a string `text` using regex


import re

text = "This this is is a a test test string"

output = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)

print(output)