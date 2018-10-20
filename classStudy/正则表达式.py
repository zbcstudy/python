import re

s = {"asxxxsd", "dsafxxf", "xxx", "dssdfds", "xxxfafaf"}

func = lambda s: re.match(r"xxx", s)

# 从输入的开始进行匹配
print(*filter(func, s))

# 匹配所有
print(*filter(lambda s: re.search(r"xxx", s), s))
