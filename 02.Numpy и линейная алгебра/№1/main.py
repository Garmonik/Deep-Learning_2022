import numpy as np

def no_numpy_mult(first, second):
    m = len(first)
    n = len(second)
    k = len(second[0])

    c = [[None for __ in range(k)] for __ in range(m)]

    for i in range(m):
        for j in range(k):       
            c[i][j] = sum(first[i][kk] * second[kk][j] for kk in range(n))
    return c

def numpy_mult(first, second):
    result = np.dot(first, second)
    return result
