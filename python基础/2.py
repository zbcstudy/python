import math
import string

sequence = [None]*10
print(sequence)

print(max([2, 4, 3]))

print(list('hello'))
print(list("hello"))

name = list("python")
# print(name[2:])
lst = [1, 2, 3]
# print(lst.append(4))

name = "hello"
print(len(name))
print(name.count("l"))

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
a.extend(b)
print(a)
print(a.pop())
print(a)
a.reverse()
print(a)

print(3*(40+2))
print(3*(40+2,))

print(tuple([1, 3, 4]))

print(math.pi)

formats = "hello %s, %s enough for ya"
values = ('word', 'yaa')
print(formats % values)

formatPi = "pi format three decimals:%.3f"
print(formatPi % math.pi)


