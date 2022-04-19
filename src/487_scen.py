#Sort a list of tuples `b` by third item in the tuple


b = [(2, 5, 3), (4, 1, 9), (6, 7, 2)]

b.sort(key=lambda x: x[2])