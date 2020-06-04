import os
import replace as r
import bigfloat
import numpy as np
file_1 = open("delete_reactions_20", 'r')
file_2 = open("delete_reactions_edit", 'w')
lib = r.replace(file_1, file_2)
file_1.close()
file_2.close()
f = open('delete_reactions_edit','r')
f1 = open('res_sec','w')
line = f.readline()
while line:
    array = []
    #print(f.readline().strip())
    f1.write(f.readline().strip())
    line = f.readline()
    for x in line.split():
        array.append(float(x))
    line = f.readline()
    for x in line.split():
        array.append(float(x))
    i = 1
    T = 6
    su = 0
    while i < 6:
        su += array[i]*T**((2*i-5)/3)
        i += 1
    su = bigfloat.exp(array[0] + array[6]*np.log(T) + su, bigfloat.precision(7))
#    su = '%.3e' % su
    #print(su)
    f1.write("\n")
    f1.write("σ = ")
    f1.write(str(su))
    f1.write("\n")
    line = f.readline()
f.close()
os.remove('delete_reactions_edit')
