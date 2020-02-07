import math
import datetime

print(math.ceil(10.2))
print(math.factorial(5))


def f1():
    f2()


def f2():
    print("f2函数")


f1()
print(datetime.date.today())
print(datetime.datetime.utcnow())
date = datetime.datetime(1994, 1, 21, 14, 23, 45)
print(date)
print(date.min)
print(date.max)
print(date.year)
print(date.isoformat())  # 采用ISO 8061 显示时间
print(date.isoweekday())  # 返回星期
print(date.strftime("%Y-%m-%d %H-%M-%S"))


# 元组可以用于返回多个值
def func(x):
    return x, x ** 3


print(func(3))

for x, y in ((1, 0), (2, 5), (3, 8)):
    print(math.hypot(x, y))

print(hash("GOD"))

ls = [2, 5, 7, 1, 6]
print(sorted(ls))
print(sorted(ls, reverse=True))

l1 = {1, 23, 4, 5, 6}
l2 = {2, 6, 8, 11, 7}
print(l1 ^ l2)
print(l1.difference(l2))
print(l1.intersection(l2))
