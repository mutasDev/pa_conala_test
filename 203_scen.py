#prepend the line '#test firstline\n' to the contents of file 'infile' and save as the file 'outfile'


with open('infile', 'r') as f:
    with open('outfile', 'w') as f1:
        f1.write('#test firstline\n')
        f1.write(f.read())