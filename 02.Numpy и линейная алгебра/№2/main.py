import numpy as np

def no_numpy_scalar(v1, v2):
    s = 0
    for v1, v2 in zip(v1, v2):
        s += v1 * v2
    return s

    return result

def numpy_scalar (v1, v2):
    result = np.dot(v1, v2)
    return result
