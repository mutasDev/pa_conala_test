#sort a list of lists 'c2' such that third row comes first
, followed by the first row and then the second row.

c2 = [[1,2,3],[4,5,6],[7,8,9]]

c2.sort(key=lambda x: x[2], reverse=True)