#selecting rows in Numpy ndarray 'a', where the value in the first column is 0 and value in the second column is 1


a = np.array([[0,1,2], [3,4,5], [6,7,8], [9,0,1]])

a[(a[:,0] == 0) & (a[:,1] == 1)]