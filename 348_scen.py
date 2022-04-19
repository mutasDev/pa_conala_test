#split string `input` based on occurrences of regex pattern '[ ](?=[A-Z]+\\b)'


import re

input = "This is a sentence with a lot of Words in it"

re.split('[ ](?=[A-Z]+\\b)', input)