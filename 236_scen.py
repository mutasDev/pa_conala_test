#replace all elements in array `A` that are not present in array `[1, 3, 4]` with zeros
.

A = [1, 2, 3, 4, 5]

for i in range(len(A)):
    if A[i] not in [1, 3, 4]:
        A[i] = 0