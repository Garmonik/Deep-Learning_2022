import numpy as np
def grad_descent_v2(func, deriv, low=None, high=None, callback=None):
    start = None
    epsilon = 0.01
    best_estimate = None
    points = []
    linspace = np.linspace(low, high, 50)
    
    for point in linspace:
        estimate = point
        
        for _ in range(150):    
            estimate -= deriv(estimate)*epsilon
            callback(estimate, func(estimate))
                
            points.append(estimate)

    points.sort(key=func)
    best_estimate = points[0]
    
    return best_estimate
