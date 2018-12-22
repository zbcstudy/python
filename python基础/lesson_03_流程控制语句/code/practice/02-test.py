# username = input("请输入用户名：")
# if username == 'admin':
#     print("欢迎管理员登录!")


print(123//100)
print(1/3)

# 判断一个数是不是质数
num = int(input("请输入一个大于1的整数："))
flag = True
i = 2
while i < num:
    if num % i == 0:
        flag = False
    i += 1
if flag:
    print(num, "是质数")
else:
    print(num, "不是质数")

# 打印1000以内的水仙花数
n = 100
while n < 1000:
    # 得到每位的数字
    # 百位
    a = n // 100
    # 十位
    b = (n - a*100) // 10
    # 个位
    c = n % 10
    if a**3 + b**3 + c**3 == n:
        print(n)
    n += 1
