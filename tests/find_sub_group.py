f = open('reaclib', 'r')
line = f.readline()
index = 1
while line:
	f.readline()
	f.readline()
	f.readline()
	line_old = line
	line = f.readline()
	line_new = line
	index += 4
	if line_new != line_old:
		print(index)
f.close()

