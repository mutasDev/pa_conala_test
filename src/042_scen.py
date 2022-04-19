#sum all elements of nested list `L`


L = [[1, 2], [3, 4], [5, 6]]

sum = 0
for i in range(len(L)):
  for j in range(len(L[i])):
    sum += L[i][j]
print(sum)