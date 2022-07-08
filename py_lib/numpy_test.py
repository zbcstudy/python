import numpy as np
from numpy import pi

a = np.array([1, 2, 3])
print(a)

b = np.array(np.matrix("1 2; 3 4"))
print(b)
print(b.ndim)
print(b.size, b.dtype)

c = np.zeros((2, 3, 4), dtype=int)
print(c)

d = np.arange(10)
print(d)

e = np.random.rand(10)
print(e)

print(np.random.randn(2, 4))

print(np.random.random(5))

print(np.ones(5, dtype=int))

f = np.eye(4)
print(f)
print(f.reshape(2, 8))

print(np.linspace(0, 1, 5))

print(np.pi)
print(np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.))
