def almost_double_factorial(n):
    if n != 0:
        m = 1 
        for i in range(m + 2, n + 1, 2):
            m *= i
    else:
        m = 1
    return m
