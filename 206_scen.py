#return `True` if string `foobarrrr` contains regex `ba[rzd]`


import re

def check_string(string, regex):
  return bool(re.search(regex, string))

print(check_string('foobarrrr', 'ba[rzd]'))