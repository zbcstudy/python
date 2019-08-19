from math import isnan
from types import MethodType


class Person(object):
    # 限制对象中的属性 使用 __slots__来限制
    __slots__ = ("height", "age")
    name = "person"

    def __init__(self, name):
        self.name = name


print(Person.name)
per = Person("tom")
print(per.name)
# 动态添加对象属性
per.age = 18
print(Person.name)
print(per.age)
print(per)
print(isnan(10))

per.height = 170
print(per.height)


# 动态添加方法
def say(self):
    print("my name is " + self.name)


per.speak = MethodType(say, per)
print(per.speak())
