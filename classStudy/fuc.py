def test(a, *b):
    print(type(b))
    for i in b:
        a = a + i
    return a


t = test(2, 3, 4, 5)
print(t)

n = 1


def func(a, b):
    global n  # 显示声明局部变量为全局变量
    n = b
    return a * b


func(2, 3)
print(n)

ls = []


def new_func(a, b):
    ls.append(b)
    return a * b


# 对于列表类型函数可以直接使用全局列表 不用使用global进行声明
s = new_func("knock-", 2)
print(s, ls)
