from math import sqrt as sq

print(sq(4))

values = 1, 2, 3
print(values)

# 增量赋值
x = 2
x += 1
x *= 2
print(x)

print("boolean: " + str(True + 2))

if x == 6:
    print(1)
else:
    print(2)

# 同一性判断
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x is y)
print(x is z)

x = 1
while x <= 10:
    print(x)
    x += 1

for number in range(23,26):
    print(number)

# 循环遍历字典元素
phoneBook = {'ace': '123', 'bcd': '234', 'cdf': '345'}
for pn in phoneBook:
    print(pn + " is " + phoneBook[pn])

name = ''
while not name:
    name = input("please enter you name: ")
    print(name)

# 循环打印列表中的元素
for n in z:
    print(n)

