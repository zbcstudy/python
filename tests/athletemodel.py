import pickle
import os
from tests import commonFunction
os.chdir("../common/person")


def put_to_store(file_list):
    all_athlete = {}
    for each_file in file_list:
        ath = commonFunction.get_file_data2(each_file)
        all_athlete[ath.name] = ath
    try:
        with open("athlete.pickle", 'wb') as athf:
            pickle.dump(all_athlete, athf)
    except IOError as err:
        print("file error" + str(err))

    return all_athlete


def get_from_store():
    all_athlete = {}
    try:
        with open("athlete.pickle", 'rb') as athf:
            all_athlete = pickle.load(athf)
    except IOError as err:
        print("file error" + str(err))
    return all_athlete


the_file_list = ['james2.txt', 'julie2.txt']
data = put_to_store(the_file_list)
print(data)

for athlete in data:
    print(athlete)
    print(data[athlete].name + " " + data[athlete].birth)


