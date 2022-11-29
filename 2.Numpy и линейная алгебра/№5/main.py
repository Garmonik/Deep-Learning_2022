import numpy as np

def transform(X, a=1):
    b = X.copy()
    b[:, 1::2] = a
    b[:, 0::2] = b[:, 0::2] ** 3
    res = np.hstack((X, b[:, ::-1]))
    return res
