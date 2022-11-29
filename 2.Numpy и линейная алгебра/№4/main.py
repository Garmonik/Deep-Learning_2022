import numpy as np

def cumsum(A):
    result = np.cumsum(A, axis=-1) 
    return result
