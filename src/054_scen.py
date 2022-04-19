#sum elements at index `column` of each list in list `data`


data = [[1,2,3], [4,5,6], [7,8,9]]
column = 2

total = 0
for row in data:
    total += row[column]
print(total)