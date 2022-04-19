#create a dictionary by adding each two adjacent elements in tuple `x` as key/value pair to it
.

x = ('a', 'b', 'c', 'd', 'e')

d = {}

for i in range(0, len(x), 2):
   d[x[i]] = x[i+1]

print(d)