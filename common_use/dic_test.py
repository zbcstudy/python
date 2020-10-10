import platform

a = {"a": 1, "b": 2}
print(a)


def dic(*args, **kwargs):
    print(args)
    print(kwargs)
    if kwargs:  # 判断参数是否有值
        items = kwargs.items()
        for item in items:
            print(item)
        print("true")
    else:
        print("false")


array = platform.architecture()
for arr in array:
    print(arr)

# dic("q")  # false
dic("q", a=1, b=2)  # true

tup = (1, 2, 3, 4)
print(list(tup))

l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
print(dict)
