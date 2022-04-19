#get a list containing the sum of each element `i` in list `l` plus the previous elements
 in the list.

l = [1,2,3,4,5]

result = []

for i in range(len(l)):
    result.append(sum(l[:i+1]))

print(result)