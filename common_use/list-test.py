import sys
import math
import os
import argparse

vec = [2, 4, 6, 1]
for x in vec:
    print(x)
vec.sort()
print(vec)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print(sys.argv)

print(sys.path)
print(os.O_RDWR)

print(math.fabs(-10))

# f = open("/")
# f.seek(-3, 2)
# f.close()

print(dir(os))

print(globals())

print(locals())

print(pow(2, 3, 4))  # 2**3/4
