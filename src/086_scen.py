#convert list of lists `L` to list of integers


L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = []
for sublist in L:
    for item in sublist:
        result.append(int(item))
print(result)