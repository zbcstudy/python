import copy

# 字典

phoneBook = {'ace': '123', 'bcd': '234', 'cdf': '345'}
print(phoneBook['ace'])

# dict用来创建字典
d = dict(name="zh", age=12)
print(d)

print('age' in d)

print(len(d))

print(d.keys())

c = copy.copy(d)
dep = copy.deepcopy(d)
cc = copy.copy(d)
c['age'] = 23
print(d)
print(c)
print(dep)

fk = {}.fromkeys('abc', 'cdf')
fk2 = {}.fromkeys(['abc', 'cdf'])
print(fk)
print(fk2)
print(fk.get('a'))

# 报错
# print(fk['f'])

print(fk.items())
ite = fk.__iter__()
print("---------------")
print(list(ite))
print(list(fk.values()))

