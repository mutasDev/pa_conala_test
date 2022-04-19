#write the elements of list `lines` concatenated by special character '\n' to file `myfile`


with open('myfile', 'w') as f:
    for line in lines:
        f.write(line + '\n')