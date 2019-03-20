import timeit

# 计算python执行时间
time = timeit.timeit("x=2+2")
print(time)

print("10次加法运算：%s" % timeit.timeit("x = sum(range(10))"))

print(sum(range(1000)))
