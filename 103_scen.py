#loop over a list `mylist` if sublists length equals 3


mylist = [[1,2,3],[4,5,6],[7,8,9]]

for sublist in mylist:
    if len(sublist) == 3:
        for item in sublist:
            print(item)