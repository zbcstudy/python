import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a * b)

# 创建一个3X3的数组
c = np.arange(9).reshape(3, 3)
print("c:\n", c)
print("-------------------")
print("a + c:\n", a + c)

bb = np.tile(b, (3, 1))
print("bb:\n", bb)
d = bb + c
print("bb + c:\n", d)

print("***********迭代************")
for x in np.nditer(d):
    print(x, end=",")
