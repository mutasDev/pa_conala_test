#find the index of a list with the first element equal to '332' within the list of lists `thelist`


thelist = [['332', 'abc', 'def'], ['111', 'ghi', 'jkl'], ['444', 'mno', 'pqr']]

for i in range(len(thelist)):
    if thelist[i][0] == '332':
        print(i)