# 遍历数组，默认情况下不进行缩进处理
def print_list(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_list(each_item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end="")
            print(each_item)


# 对时间字符串进行处理，修改成统一格式
def senitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + "." + secs


# 数组删除重复数据
def get_unique(get_list):
    unique = []
    for each_l in get_list:
        if each_l not in unique:
            unique.append(each_l)
    return unique


# 获取文件数据
def get_file_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
            return data.strip().split(",")
    except IOError as err:
        print("file error" + str(err))
        return None


# 获取文件数据2:处理数据更加方便
def get_file_data2(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
            temp = data.strip().split(",")
            # return {'name': temp.pop(0), 'birth': temp.pop(0), "times": sorted(set([senitize(t) for t in temp]))[0:3]}
            # return Athlete(temp.pop(0), temp.pop(0), temp)
            return AthleteList(temp.pop(0), temp.pop(0), temp)
    except IOError as err:
        print("file error" + str(err))
        return None


# 创建一个类用来描述对象
class Athlete:
    def __init__(self, a_name, a_birth=None, a_times=[]):
        Athlete.name = a_name
        Athlete.birth = a_birth
        Athlete.times = a_times

    def top3(self):
        return sorted(set([senitize(t) for t in self.times]))[0:3]

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, list_of_time):
        self.times.extend(list_of_time)


class AthleteList(list):
    def __init__(self, a_name, a_birth=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.birth = a_birth
        self.extend(a_times)

    def top3(self):
        return sorted(set([senitize(t) for t in self]))[0:3]


class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name




