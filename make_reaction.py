f = open("delete_reactions_all", 'r')
line = f.readline()
index = 1
while line:
	f1 = open("delete_reactions_" + str(index), 'w')
	i = 0
	while i <= 3:
		f1.write(line)
		line = f.readline()
		i += 1
	f1.close()
	index += 1
f.close()
	
