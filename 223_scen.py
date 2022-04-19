#convert items in `T1` to integers
 and sum them

T1 = [1, 2, 3, 4, 5]

result = 0
for i in T1:
    result += int(i)
print(result)