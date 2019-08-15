class Person(object):
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

