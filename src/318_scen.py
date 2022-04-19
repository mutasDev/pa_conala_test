#get whatever is between parentheses as a single match, and any char outside as an individual match in string '(zyx)bc'


import re

result = re.findall(r'\((.*?)\)', '(zyx)bc')
print(result)