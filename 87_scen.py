#combine elements of each list in list `L` into digits of a single integer
.

L = [[1, 2], [3, 4], [5, 6]]

int_L = int("".join(str(i) for i in L))