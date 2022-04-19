#Find all numbers and dots from a string `text` using regex


import re

text = "This is a text with 2 numbers 34 and 567"

regex = '[0-9.]+'

matches = re.findall(regex, text)

print(matches)