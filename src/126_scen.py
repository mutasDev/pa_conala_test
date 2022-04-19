#count the occurrences of item "b" in list `l`


l = ['a', 'b', 'c', 'b', 'd', 'b']

count = 0
for item in l:
    if item == 'b':
        count += 1

print(count)