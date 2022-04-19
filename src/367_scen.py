#find all matches of regex pattern '([a-fA-F\\d]{32})' in string `data`


import re

data = "af0012d3b56789012345678901234567"

pattern = '([a-fA-F\\d]{32})'

 matches = re.findall(pattern, data)

print(matches)