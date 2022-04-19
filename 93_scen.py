#search for string that matches regular expression pattern '(?<!Distillr)\\\\AcroTray\\.exe' in string 'C:\\SomeDir\\AcroTray.exe'


import re

string = 'C:\\SomeDir\\AcroTray.exe'
pattern = '(?<!Distillr)\\\\AcroTray\\.exe'

result = re.search(pattern, string)

if result:
  print("Match found: %s" % result.group())
else:
  print("No match found")