#Get all matches with regex pattern `\\d+[xX]` in list of string `teststr`


import re

teststr = ['abc1234', 'def5678', 'ghi9012', 'jkl3456']

for item in teststr:
    if re.search('\\d+[xX]', item):
        print(item)