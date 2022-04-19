#python regex  to find all numbers and dots from 'text'


import re

text = "This is a text with 2.5 and 4.7 and 3"

numbers_and_dots = re.findall("[0-9.]+", text)

print(numbers_and_dots)