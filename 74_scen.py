#print a list `l` and move first 3 elements to the end of the list


l = [1, 2, 3, 4, 5]

l.extend(l[:3])

del l[:3]

print(l)