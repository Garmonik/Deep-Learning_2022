def numerical_derivative_2d(f, epsilon):
    def grad_func(a):
        x, y = a
        df_x = (f(np.array([x+epsilon, y])) - f(a))/epsilon
        df_y = (f(np.array([x, y+epsilon])) - f(a))/epsilon

        return np.array([df_x, df_y])

    return grad_func


def grad_descent_2d(func, low, high, start=None, callback=None):
    eps = 1e-6
    df = numerical_derivative_2d(func, eps)

    iter_num = int(1e+4)
    lr=0.5
    x = np.array([0, 0])
    for i in range(iter_num):
        x = x - lr * df(x)
        x = np.clip(x, low, high)
    return x
