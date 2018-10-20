import os
from tests import commonFunction

os.chdir("../common/person")

james = commonFunction.get_file_data("james2.txt")
# (james_name, james_birth) = (james.pop(0), james.pop(0))
# print(james_name, james_birth)
# data = sorted(set([commonFunction.senitize(t) for t in james]))[0:3]
# print(data)

# dir = {}
# print(type(dir))
# plan = dict()
# print(type(plan))

james_data = {}
james_data['name'] = james.pop(0)
james_data['birth'] = james.pop(0)
james_data['times'] = james
print(james_data['name'] + "\'s fast time is" + str(sorted(set([commonFunction.senitize(t) for t in james_data['times']]))[0:3]))

# julie = commonFunction.get_file_data2("julie2.txt")
# print(julie['name'] + "\'s fast time is" + str(julie['times'][0:3]))

mikey = commonFunction.get_file_data2("mikey2.txt")
print(mikey.name + "\'s fast time is" + str(mikey.top3()))

vare = commonFunction.Athlete('vare vi')
vare.add_time('3.12')
print(vare.top3())

vare.add_times(['2.14', '3.33', '4.5'])
print(vare.top3())

# 类的继承关系
Jonney = commonFunction.NamedList("jonn ted")
print(Jonney.name)
print(type(Jonney))
print(dir(Jonney))

sarah = commonFunction.get_file_data2("sarah2.txt")
print(sarah.name + "\'s fast time is" + str(sarah.top3()))
