# coding:utf-8
import os
print(os.getcwd())
os.chdir("../common")

man = []
other = []

try:
    data = open("sketch.txt")
    man_file = open("man.txt", "w+")
    other_file = open("other.txt", "w+")
    for line_speak in data:
        if not line_speak.find(":") == -1:
            (role, role_speak) = line_speak.split(":", 1)
            speaks = role_speak.strip()
            if role == 'Man':
                man_file.write(speaks)
            elif role == 'Other Man':
                other_file.write(speaks)
except IOError as err:
    print("file error" + str(err))
finally:
    if "data" in locals():
        data.close()
    if "man_file" in locals():
        man_file.close()
    if "other" in locals():
        other_file.close()


for num in range(4):
    print(num)
