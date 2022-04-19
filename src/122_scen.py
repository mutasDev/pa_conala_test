#count the occurrences of item "a" in list `l`


l = ['a', 'b', 'a', 'c', 'd', 'a']

count = 0
for item in l:
    if item == 'a':
        count += 1

print(count)