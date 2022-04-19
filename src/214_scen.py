#convert each tuple in list `l` to a string with '@' separating the tuples' elements


l = [(1,2), (3,4), (5,6)]

for t in l:
    print('@'.join(map(str, t)))