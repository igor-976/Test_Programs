f = open('reaclib_with_del')
line = f.readline()
index = 1
all_index = []


def find(nuc, lin):
    if lin.find(nuc) != -1:
        all_index.append(index)

while line:
    find("kr78  he4 se74", line)
    find("sr84  he4 kr80", line)
    find("sn112  he4cd108", line)
    find("xe124  he4te120", line)
    find("ba130  he4xe126", line)
    find("ce136  he4ba132", line)
    find("he4 se74 kr78 ", line)
    find("he4 kr80 sr84", line)
    find("he4cd108sn112", line)
    find("he4te120xe124", line)
    find("he4xe126ba130", line)
    find("he4ba132ce136", line)

    line = f.readline()
    index += 1

print(all_index)
print("Number of nuclids is", len(all_index))
