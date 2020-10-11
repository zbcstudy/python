from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2 + 10 * np.sin(x)


if __name__ == '__main__':
    # 绘制目标函数图形
    plt.figure(figsize=(10, 5))
    x = np.arange(-10, 10, 0.1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("optimize")
    plt.plot(x, f(x), 'r-', label='$f(x)=x^2 + 10*sin(x)')
    # 图像中的最低点函数值
    a = f(-1.3)
    optimize.fmin_bfgs(f, 0)
    grid = (-10, 10, 0.1)
    print(optimize.brute(f, (grid,)))  # 全局最小值
    plt.annotate('min', xy=(-1.3, a), xytext=(3, 40), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.legend()
    plt.show()

