#match regex '\\((.*?)\\)|(\\w)' with string '(zyx)bc'


import re

pattern = re.compile(r'\((.*?)\)|(\w)')

match = pattern.match('(zyx)bc')

if match:
    print(match.group(1))
    print(match.group(2))