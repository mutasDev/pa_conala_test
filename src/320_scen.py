#match multiple regex patterns with the alternation operator `|` in a string `(zyx)bc`


import re

pattern1 = re.compile('z')
pattern2 = re.compile('y')
pattern3 = re.compile('x')

if pattern1.match('(zyx)bc') or pattern2.match('(zyx)bc') or pattern3.match('(zyx)bc'):
  print('Match found!')
else:
  print('No match found.')