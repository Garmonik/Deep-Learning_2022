def grad_descent_v1(func, deriv, start=None, callback=None):
    if start is None:
        np.random.seed(179)
        start = np.random.randn()

    estimate = start
    i = 1
    a = 0.01
    while (deriv(estimate)**2 > (1e-2)**2) and (i < 1000):
        estimate = estimate - a * deriv(estimate)
        i += 1
    return estimate
