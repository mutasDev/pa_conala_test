#shuffle columns of an numpy array 'r'


import numpy as np

def shuffle_columns(r):
    np.random.shuffle(r.T)
    return r