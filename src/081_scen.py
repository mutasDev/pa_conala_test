#print a 2 dimensional list `tab` as a table with delimiters


tab = [[1,2,3], [4,5,6], [7,8,9]]

for row in tab:
    print(' | '.join([str(col) for col in row]))
    print('-' * len(row))