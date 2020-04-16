f=open('reactions.txt')
#w = str(input())
#if w == "reaclib":
#    f = open('reaclib', 'r')
#else:
#    f = open('reaclib_new', 'r')
line = f.readline()
index = 1
all_index = []
x=0
y=40
while line:
    if line.find("br78",x,y) != -1:
        all_index.append(index)
    if line.find("br80",x,y) != -1:
        all_index.append(index)
    if line.find("rb84",x,y) != -1:
        all_index.append(index)
    if line.find("ag106",x,y) != -1:
        all_index.append(index)
    if line.find("ag108",x,y) != -1:
        all_index.append(index)
    if line.find("in112",x,y) != -1:
        all_index.append(index)
    if line.find("in114",x,y) != -1:
        all_index.append(index)
    if line.find("sb120",x,y) != -1:
        all_index.append(index)
    if line.find("i124",x,y) != -1:
        all_index.append(index)
    if line.find("i126",x,y) != -1:
        all_index.append(index)
    if line.find("cs130",x,y) != -1:
        all_index.append(index)
    if line.find("cs132",x,y) != -1:
        all_index.append(index)
    if line.find("la136",x,y) != -1:
        all_index.append(index)
    if line.find("ho164",x,y) != -1:
        all_index.append(index)
    line = f.readline()
    index += 1
#print(index)
print(all_index)
print("Number of nuclids is", len(all_index))
