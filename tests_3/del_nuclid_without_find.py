import find_func as s
k = 0
all_index = s.find_nuc("reaclib_with_del_ob", "reaction", 15,  40, 320389)
f = open('reaclib_with_del_ob', 'r',).readlines()
f1 = open("delete_react_ob", 'w')
for i in all_index:
    i -= k
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    f1.write(f.pop(i-2))
    k += 4
with open("reaclib_with_del_ob2", 'w') as F:
    F.writelines(f)
