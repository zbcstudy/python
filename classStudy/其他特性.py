filter_me = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda x: x % 2 == 0, filter_me)
print(*result)

func = lambda x: x % 2 == 0
result = filter(func, filter_me)
print(*result)

f = range(1, 10)
print(*f)
