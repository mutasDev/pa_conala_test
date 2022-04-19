#delete all characters "i" in string "it is icy"


string = "it is icy"

for i in string:
    if i == "i":
        string = string.replace(i, "")

print(string)