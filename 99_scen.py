#lower a string `text` and remove non-alphanumeric characters aside from space
.

text = text.lower()
text = text.replace(" ", "")
for char in text:
 if char.isalnum() == False:
  text = text.replace(char, "")