#How to delete all instances of a character in a string in python?


string = "Hello, world!"

for char in string:
    if char == 'l':
        string = string.replace(char, '')

print(string)