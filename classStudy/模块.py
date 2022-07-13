import os

print(dir(os))

print('os.path:', os.path)

print(os.getcwd())

print(os.listdir("."))

file_list = sorted(os.listdir("."))
