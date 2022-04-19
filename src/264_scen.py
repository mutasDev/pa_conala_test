#find 10 largest differences between each respective elements of list `l1` and list `l2`


l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [10,9,8,7,6,5,4,3,2,1]

def largest_difference(l1, l2): 
    diff = []
    for i in range(len(l1)):
        diff.append(abs(l1[i]-l2[i]))
    diff.sort()
    return diff[-10:]

print(largest_difference(l1, l2))