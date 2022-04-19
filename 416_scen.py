#delete all occurrences of character 'i' in string 'it is icy'


string = "it is icy"

for char in string:
  if char == "i":
    string = string.replace(char, "")

print(string)