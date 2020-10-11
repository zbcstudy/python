#  非线性最小二乘拟合
from scipy import optimize
import numpy as np
from common_use.ml import scipy_test

x_data = np.linspace(-10, 10, num=20)
y_data = scipy_test.f(x_data) + np.random.randn(x_data.size)


def f2(x, a, b):
    return a * x ** 2 + b * np.sin(x)


guss = [2, 2]
params, params_covariance = optimize.curve_fit(f2, x_data, y_data, guss)

print(params, params_covariance)

