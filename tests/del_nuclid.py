f = open('nfis', 'r',)
line = f.readline()
index = 1
all_index = []
k = 0
while line:
    if line.find("br78", 15, 40) != -1:
        all_index.append(index)
    if line.find("br80", 15, 40) != -1:
        all_index.append(index)
    if line.find("rb84", 15, 40) != -1:
        all_index.append(index)
    if line.find("ag106", 15, 40) != -1:
        all_index.append(index)
    if line.find("ag108", 15, 40) != -1:
        all_index.append(index)
    if line.find("in112", 15, 40) != -1:
        all_index.append(index)
    if line.find("in114", 15, 40) != -1:
        all_index.append(index)
    if line.find("sb120", 15, 40) != -1:
        all_index.append(index)
    if line.find("i124", 15, 40) != -1:
        all_index.append(index)
    if line.find("i126", 15, 40) != -1:
        all_index.append(index)
    if line.find("cs130", 15, 40) != -1:
        all_index.append(index)
    if line.find("cs132", 15, 40) != -1:
        all_index.append(index)
    if line.find("la136", 15, 40) != -1:
        all_index.append(index)
    if line.find("ho164", 15, 40) != -1:
        all_index.append(index)
    line = f.readline()
    index += 1
f.close()
f = open('nfis', 'r',).readlines()
f1 = open("del.txt", 'w')
for i in all_index:
    i -= k
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    k += 4
with open("nfis_with_del", 'w') as F:
    F.writelines(f)
