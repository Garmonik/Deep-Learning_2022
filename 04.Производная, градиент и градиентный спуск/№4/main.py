def grad_descent_v2(func, deriv, low=None, high=None, callback=None):
    estimate = (low + high) / 2
    i = 1
    a = 0.01
    while (deriv(estimate)**2 > (1e-2)**2) and (i < 1000):
        estimate = np.clip(estimate, low, high)   
        estimate = estimate - a * deriv(estimate)
        i += 1
    estimate1 = estimate
    estimate = high
    i = 1
    a = 0.01
    while (deriv(estimate)**2 > (1e-2)**2) and (i < 1000):
        estimate = np.clip(estimate, low, high)   
        estimate = estimate + a * deriv(estimate)
        i += 1
    estimate2 = estimate
    if func(estimate2) >= func(estimate1):
        return estimate1
    return estimate2
