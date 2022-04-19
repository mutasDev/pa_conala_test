#search for occurrences of regex pattern '>.*<' in xml string `line`
 and returns the list of matches

import re

matches = re.findall(">.*<", line)

print(matches)