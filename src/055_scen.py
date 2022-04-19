#sum columns of a list `array`


array = [[1,2,3], [4,5,6], [7,8,9]]

def sum_columns(array):

total = 0

for row in array:

for column in row:

total += column

return total