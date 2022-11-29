import numpy as np #не стирать!        

def diag_2k(a):
    b = np.diag(a)
    sum = 0
    for i in range(b.size):
        if b[i] % 2 == 0:
            sum += b[i]
    return sum
