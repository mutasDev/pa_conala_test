#read a file `file` without newlines


with open("file", "r") as f:
    for line in f:
        print(line, end="")