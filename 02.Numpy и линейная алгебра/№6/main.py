import numpy as np

def encode(a):
    b = a.copy()
    b = np.insert(b, 0, b[0] - 1)
    b = np.ravel(b)
    b = np.diff(b)
    c = np.nonzero(b)
    c = np.ravel(c)


    d = a.copy()
    d = np.insert(d, 0, d[0] - 1)
    d = np.append(d, d[0] - 1)
    d = np.ravel(d)
    d = np.diff(d)
    e = np.nonzero(d)
    e = np.ravel(e)

    result = (a[c], np.diff(e))
    return result
