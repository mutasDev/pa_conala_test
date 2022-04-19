#Multiply a matrix `P` with a 3d tensor `T` in scipy


import numpy as np
from scipy import signal

P = np.array([[1, 2, 3], [4, 5, 6]])
T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

result = signal.convolve(P, T, mode='valid')

print(result)