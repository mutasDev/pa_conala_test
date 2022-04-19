#convert list of tuples `L` to a string


L = [('a', 1), ('b', 2), ('c', 3)]

result = ''
for t in L:
    result += t[0] + ':' + str(t[1]) + ','

print(result[:-1])