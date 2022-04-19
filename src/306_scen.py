#append each line in file `myfile` into a list


with open('myfile') as f:
    lines = [line.rstrip('\n') for line in f]