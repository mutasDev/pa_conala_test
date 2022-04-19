#Use a regex to get all text in a string `example_str` that is not surrounded by square brackets
.

import re

example_str = "This is an [example] string."

result = re.sub(r"\[(.*?)\]", "", example_str)

print(result)