#Retrieve each line from a file 'File.txt' as a list
 of words

with open('File.txt') as f:
    lines = [line.split() for line in f]