#open a file `Output.txt` in append mode
 and writes the following line to it:

"This is the first line of the file"

f = open("Output.txt", "a")
f.write("This is the first line of the file")
f.close()