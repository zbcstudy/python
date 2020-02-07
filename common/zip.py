import sys

filePath = "../common/data.txt"
contracts = []
input_string = ["1", "34", "123", "22", "5"]


def zip_fuc():
    with open(filePath) as file:
        header = file.readline().strip().split("\t")
        for line in file:
            line = line.strip().split("\t")
            contract_map = zip(header, line)
            contracts.append(dict(contract_map))
        print(contracts)
        for contract in contracts:
            print("email:{email}--{last}--{first}".format(**contract))


def sys_p():
    print(sys.argv)
    output_int = [int(n) for n in input_string]
    print(output_int)
    output_int2 = [int(n) for n in input_string if len(n) < 3]
    print(output_int2)
    print(sorted(output_int2))


if __name__ == '__main__':
    sys_p()
