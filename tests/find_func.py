def find_nuc(file_read, file_write, initial_point, end_point, final_index):
    f = open(file_read, 'r')
    f1 = open(file_write, 'w')
    line = f.readline()
    index = 1
    all_index = []
    do_tab = 1
    while index <= final_index:
        if line.find("kr78", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("kr80", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("cd106", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("cd108", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("sn112", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("sn114", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("er164", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("te120", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("xe124", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("xe126", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("ba130", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("ba132", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("sr84", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("ce136", initial_point, end_point) != -1:
            all_index.append(index)
            if do_tab:
                line = line.lstrip()
            f1.write(line)
            f1.write('\n')
        if line.find("se74", initial_point, end_point) != -1:
            all_index.append(index)
        line = f.readline()
        index += 1
        #print(index)
    print(all_index)
    print("Number of nuclids is", len(all_index))
    f1.close()
    f.close()
    return 0
