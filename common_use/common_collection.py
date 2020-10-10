from collections import deque, defaultdict
import collections

users = ['liu1', 'liu2', 'liu3', 'liu1', 'liu1', 'liu2']
user_dict = {}
for user in users:
    if user in user_dict:
        user_dict[user] += 1
    else:
        user_dict[user] = 1

print(user_dict)

user_dict2 = {}
for user in users:
    user_dict2.setdefault(user, 0)
    user_dict2[user] += 1

print(user_dict2)

# 使用defaultdict
user_dict3 = defaultdict(int)
for user in users:
    user_dict3[user] += 1

print(user_dict3)


# deque
a = [1, 2, 3]
a_deque = deque(a)
print(a_deque)

c = {"a": 1, "b": 2, "c": 4}
# 将dic转化成deque
c_deque = deque(c)
print(c_deque)

print(dir(collections))



