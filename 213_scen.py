#convert elements of each tuple in list `l` into a string  separated by character `@`


l = [(1,2), (3,4), (5,6)]

for t in l:
    print('@'.join(map(str, t)))