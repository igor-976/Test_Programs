f=open('reaclib')

line = f.readline()
index = 1
all_index = []
x=15
y=40
final_index = 310000


#while index <= 127500:
#        line = f.readline()
#        index += 1
	
while index <= final_index:

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
