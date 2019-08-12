import numpy as np

a = [1, 2, 3]
b = [i + 1 for i in a]
print(b)


def numpy_sum(n):
    a = np.arange(n) ** 3
    print(a)


numpy_sum(3)

array = np.array([0, 1, 2, 3, 4])
print(array.shape)


if __name__ == '__main__':
    print("主程序文件")
