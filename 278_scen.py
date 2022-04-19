#get the item at index 0 from the tuple that has maximum value at index 1 in list `lis`


lis = [(1,2),(3,4),(5,6)]

max(lis, key=lambda x: x[1])[0]