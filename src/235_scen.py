#remove any url within string `text`


text = "Please visit http://www.example.com and http://www.python.org"

result = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
print(result)