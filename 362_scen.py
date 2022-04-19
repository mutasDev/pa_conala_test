#extract attributes 'src="js/([^"]*\\bjquery\\b[^"]*)"' from string `data`


import re

data = '<script src="js/jquery.js"></script>'

pattern = 'src="js/([^"]*\\bjquery\\b[^"]*)"'

result = re.search(pattern, data)

print(result.group(1))