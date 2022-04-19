#Python split a string using regex


import re

def split_string(text):

return re.split('\W+', text)