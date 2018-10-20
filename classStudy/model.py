from classStudy import Fridge
import sys
import os
import shutil

print(sys.path)

print(list(sys.modules.keys()))

print(Fridge.Fridge.__name__)


def make_text_file():
    if os.path.isfile("first.txt"):
        print("you are trying to create a file that already exist!")
    else:
        a = open("first.txt", "w")
        a.write("this is how you create a new file")
        a.close()


# 参数a 表示不会覆盖原先存在的文本，只会将新的文本添加
def add_some_text():
    a = open("first.txt", "a")
    a.write("\nanother text")
    a.close()


def print_line_length():
    a = open("first.txt", "r")
    text = a.readlines()
    for line in text:
        print(len(line))


# make_text_file()
# add_some_text()

f = open("first.txt", "r")
# print(f.readline())
print(f.read())

print_line_length()

print(os.path.split("‪C:\Python36\Lib\http\client.py"))
(first, last) = os.path.split("‪C:\Python36\Lib\http\client.py")
print(first)
print(last)


# 分解路径
def split_fully(path):
    parent_path, name = os.path.split(path)
    if name == "":
        return (parent_path,)
    else:
        return split_fully(parent_path) + (name,)


print(split_fully("‪C:\\Python36\\Lib\\http\\client.py"))

# 提取扩展名
parts = os.path.splitext("image.jpg")
print(parts)
extension = parts[1]
print(extension)

# 获取目录下的文件列表
print(os.listdir("C:\Python36\Lib\http"))


# 打印目录下的文件和子目录的完整路径
def print_fully_dir(path):
    names = os.listdir(path)
    for name in names:
        print(os.path.join(path + name))


print_fully_dir("C:\Python36\Lib\http")

# 获取文件信息
answer = os.path.isfile("C:\Python36\Lib\http")
print(answer)

b = os.path.isdir("C:\Python36\Lib\http")
print(b)

# shutil.move("test.html", "../common")


