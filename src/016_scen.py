#Calculate sum over all rows of 2D numpy array


import numpy as np 
  
# 2D numpy array 
arr = np.array([[1, 2, 3], 
                [4, 5, 6]]) 
  
# sum over all rows 
print(arr.sum(axis = 1))