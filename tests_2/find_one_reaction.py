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
    line = f.readline()
    index += 1

print(all_index)
print("Number of nuclids is", len(all_index))
