# coding:utf-8
import os
print(os.getcwd())
os.chdir("../common")
print(os.getcwd())

# 打开数据文件，读取一行数据
data = open("sketch.txt")
print(data.readline())

print(data.readline())

# 回到文件的起始位置
data.seek(0)
# print data.seek(0)

# 遍历文件中的数据
# print each_line
for each_line in data:
    if not each_line.find(":") == -1:
        (role, line_speak) = each_line.split(":", 1)
        print(role + " said:" + line_speak)

# 异常处理
for each_line_2 in data:
    try:
        (role, line_speak) = each_line.split(":", 1)
        print(role + " said:" + line_speak)
    except:
        pass

man = []
other = []

try:
    data = open("sketch.txt")
    for each_line_3 in data:
        try:
            (role, line_speak) = each_line_3.split(":", 1)
            other_speak = line_speak.strip()
            if role == 'Man':
                man.append(other_speak)
            elif role == 'Other Man':
                other.append(other_speak)
        except ValueError:
            pass
    data.close()
except IOError:
    print("file is missing !")

print(man)
print(other)

# 写数据到指定文件
try:
    out = open("out.txt", "w+")
    data = open("sketch.txt")
    for write_line in data:
        out.write(write_line)
    out.close()
except IOError as err:
    print("FILE ERROR:" + str(err))
finally:
    if "out" in locals(): out.close()
    if "data" in locals():data.close()

data.close()

