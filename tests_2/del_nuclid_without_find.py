import find_nuc_func as s
k = 0
all_index = s.all_index
f = open('reaclib_with_del1', 'r',).readlines()
f1 = open("delete_react_2", 'w')
for i in all_index:
    i -= k
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    k += 4
with open("reaclib_with_del", 'w') as F:
    F.writelines(f)
