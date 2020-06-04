def replace(file_1, file_2):
	line = file_1.readline()
	while line:
		edit_line_1 = line.replace("-", " -")
		edit_line_2 = edit_line_1.replace("e ", "e")
		edit_line_2 = edit_line_2.replace("E ", "E")
		file_2.write(edit_line_2)
		line = file_1.readline()
#file_1 = open("delete_reactions", 'r')
#file_2 = open("delete_reactions_edit", 'w')
#replace(file_1, file_2)

