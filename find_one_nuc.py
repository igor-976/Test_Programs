def find_reactions(first_type, nuclid):
    if (first_type):
        f=open('reaclib')
        line = f.readline()
        index = 1
        all_index = []
        x=10
        y=40
        final_index = 127000
        while index <= final_index:
            if line.find(nuclid,x,y) != -1:
    	        all_index.append(index)
            line = f.readline()
            index += 1
        return all_index

    else:
        f=open('reaclib')
        index = 0
        final_index = 127000
        while index <= final_index:
            line = f.readline()
            index += 1
        all_index = []
        x=15
        y=40
        final_index = 330000
        while index <= final_index:
            if line.find(nuclid,x,y) != -1:
    	        all_index.append(index)
            line = f.readline()
            index += 1
        return all_index
#print((find_reactions(True, "br78")))
