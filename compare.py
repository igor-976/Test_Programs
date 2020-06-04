import pandas as pd

array_of_interesting_nucldies_mother = [
    "cd106",
    "cd108",
    " kr78",
    " kr80",
    "ba130",
    "ba132",
    "er164",
    "xe124",
    "xe126",
    "sn112",
    "sn114",
    "ce136",
    " sr84",
    "te120",
    " se74",
    "hf136"
]

dictionary = {
    "cd": 48,
    "kr": 36,
    "ba": 56,
    "er": 68,
    "xe": 54,
    "sn": 50,
    "ce": 58,
    "sr": 38,
    "te": 43,
    "se": 34,
    "hf": 72
}

experimental_data = {
    "74|34": 0.580,
    "78|36": 0.146,
    "80|36": 0.940,
    "84|38": 0.128,
    "92|42": 0.634,
    "94|42": 0.361,
    "96|44": 0.105,
    "98|44": 0.036,
    "102|46": 0.013,
    "106|48": 0.019,
    "108|48": 0.014,
    "110|48": 0.020,
    "112|50": 0.036,
    "114|50": 0.024,
    "120|52": 5.8e-3,
    "124|54": 7.4e-3,
    "126|54": 6.7e-3,
    "130|56": 4.8e-3,
    "132|56": 4.7e-3,
    "136|58": 2.3e-3,
    "138|58": 3e-3,
    "144|62": 7.4e-3,
    "152|64": 8.4e-4,
    "156|66": 1.9e-4,
    "158|66": 3.3e-4,
    "162|68": 3.1e-4,
    "164|68": 3.6e-3,
    "168|70": 2.4e-4,
    "174|72": 3.1e-4,
    "180|74": 4e-4,
    "184|76": 1.2e-4,
    "190|78": 1.8e-4,
    "196|80": 3.1e-4
}

def compare_h5(fn1, fn2, index_res):
    def get_index(store, a, z):
        if (isinstance(store, pd.HDFStore)):
            sa = pd.Series(store.root.A)
            sz = pd.Series(store.root.Z)
            a_arr = sa[sa == a].keys()
            z_arr = sz[sz == z].keys()
            index = a_arr.intersection(z_arr)
            if (len(index) == 1):
                return index[0]
            else:
                raise "Not found element"
        else:
            raise "Error"

    store1 = pd.io.pytables.HDFStore(fn1)
    store2 = pd.io.pytables.HDFStore(fn2)
    file_x = open('out_res/res_' + str(index_res),'w')
    
    for index in range(0, len(array_of_interesting_nucldies_mother)):
        # item_for_compare = 'kr78'
        elem_name = array_of_interesting_nucldies_mother[index]
        z = dictionary[''.join(x for x in elem_name if x.isalpha())]        
        # z_compare = dictionary[''.join(x for x in item_for_compare if x.isalpha())]
        a = int(''.join(x for x in elem_name if x.isdigit()))
        # a_compare = int(''.join(x for x in item_for_compare if x.isdigit()))
        elem_index = get_index(store1, a, z)
        size_t1, _ = store1.root.Y.shape
        y1 = store1.root.Y[size_t1 - 1][elem_index]
        size_t2, _ = store2.root.Y.shape
        y2 = store2.root.Y[size_t2 - 1][elem_index]
        print("{0}, WithMy: {1}, WithoutMy: {2}".format(elem_name, y1, y2))
        file_x.write("{0}, WithMy: {1}, WithoutMy: {2}".format(elem_name, y1, y2))
        file_x.write('\n')
	
    store1.close()
    store2.close()

folder_name = 'out-r'
for index in range(1, 2):
    compare_h5(folder_name + '/WithMy-' + str(index) + '.h5', 
        folder_name + '/WithoutMy-' + str(index) + '.h5', 14)
