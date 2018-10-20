from tests import commonFunction
import os

# 获取需要处理的文件的路径
path = os.getcwd()
print(os.getcwd())
os.chdir("../common/person")

try:
    with open("james.txt") as jaf:
        data = jaf.readline()
        james = data.strip().split(",")
    with open("julie.txt") as juf:
        data = juf.readline()
        julie = data.strip().split(",")
    with open("mikey.txt") as mif:
        data = mif.readline()
        mikey = data.strip().split(",")
    with open("sarah.txt") as saf:
        data = saf.readline()
        sarah = data.strip().split(",")
    print(sorted(james))
    print(sorted(julie))
    print(sorted(mikey))
    print(sorted(sarah))
    print("-------------------------------------------------")
    clean_james = []
    clean_julie = []
    clean_mikey = []
    clean_sarah = []

    for clean_d in james:
        clean_james.append(commonFunction.senitize(clean_d))
    for clean_d in julie:
        clean_julie.append(commonFunction.senitize(clean_d))
    for clean_d in mikey:
        clean_mikey.append(commonFunction.senitize(clean_d))
    for clean_d in sarah:
        clean_sarah.append(commonFunction.senitize(clean_d))

    print(sorted(clean_james))
    print(sorted(clean_julie))
    print(sorted(clean_mikey))
    print(sorted(clean_sarah))
    print("-------------------------------------------------")

# 列表推导功能会完成上方重复的代码的功能
    print(sorted([commonFunction.senitize(t) for t in james]))
    print(sorted([commonFunction.senitize(t) for t in julie]))
    print(sorted([commonFunction.senitize(t) for t in mikey]))
    print(sorted([commonFunction.senitize(t) for t in sarah]))
    print("-------------------------------------------------")

    # unique_james = []
    # unique_julie = []
    # unique_mikey = []
    # unique_sarah = []
    unique_james = commonFunction.get_unique(sorted([commonFunction.senitize(t) for t in james]))
    unique_julie = commonFunction.get_unique(sorted([commonFunction.senitize(t) for t in julie]))
    unique_mikey = commonFunction.get_unique(sorted([commonFunction.senitize(t) for t in mikey]))
    unique_sarah = commonFunction.get_unique(sorted([commonFunction.senitize(t) for t in sarah]))

    print(unique_james[0:3])
    print(unique_julie[0:3])
    print(unique_mikey[0:3])
    print(unique_sarah[0:3])
    print("--------------------------------------------------")

# 集合set不允许出现重复数据
    print(sorted(set([commonFunction.senitize(t) for t in james])))

except IOError as err:
    print("file is error" + str(err))





