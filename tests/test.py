# coding:utf-8
import json
from tests import commonFunction
print("hello world")
if 43 > 42:
    print("zhaobicheng")

cast = ["abc", "def", "qwe"]
print(cast[1])
cast.extend(["asd"])
print(cast)
# for for_cast in cast:
#     print for_cast

# isinstance 内置方法，判断数据类型
cast = ["abc", "def", "qwe", ["zxc", "ddd", ["zha", "bi"]], "fdf"]
print("------------------------------")
print(json.dumps(cast))
# for for_cast in cast:
#     if isinstance(for_cast, list):
#         for for_cast_2 in for_cast:
#             print for_cast_2
#     else:
#         print for_cast

# def print_list(the_list):
#     for each_item in the_list:
#         if isinstance(each_item, list):
#             print_list(each_item)
#         else:
#             print each_item

commonFunction.print_list(cast, 0)

a = 10
b = 20
print("A add to B is %s" % (a+b))


def type_test(input_text):
    return type(input_text) == str


print(type_test("dsf"))
