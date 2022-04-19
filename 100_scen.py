#remove all non-alphanumeric characters except space from a string `text` and lower it


text = "The quick brown fox jumps over the lazy dog"

text = text.lower()

text = text.replace(" ", "")

for char in text:

if char.isalnum():

text = text.replace(char, "")

print(text)