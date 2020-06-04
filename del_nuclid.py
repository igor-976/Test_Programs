import find_one_nuc as s
k = 0
nuclid_1 = "sn114"
#nuclid_2 = "in114"
all_index_1 = s.find_reactions(True, nuclid_1)
all_index_2 = s.find_reactions(False, nuclid_1)
#all_index_3 = s.find_reactions(True, nuclid_2)
#all_index_4 = s.find_reactions(False, nuclid_2)

all_index = all_index_1 + all_index_2 
#+ all_index_3 + all_index_4
all_index.sort()
#print(all_index)

f = open('reaclib', 'r',).readlines()
f1 = open("delete_reactions_all", 'w')
for i in all_index:
    i -= k
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    k += 4
with open("reaclib_with_del", 'w') as F:
    F.writelines(f)
