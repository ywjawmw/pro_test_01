# coding: utf-8

"""
@function: 处理药方匹配的train和valid文件
"""


def dataSplit(file_name):
    print("分割sym-herb file !!!")
    print('***************开始构建sym-herb train set and test set！！！************')
    lines = open(file_name, 'r').readlines()
    herb_id = []
    sym_id = []
    for line in lines:
        sym_herb = line.split("\t")
        sym_id.append(sym_herb[0])
        herb_id.append(sym_herb[1])
    return sym_id, herb_id


def dataMap(file_name, file_path, sym_id, herb_id):
    print("开始map %s" % file_name)
    lines = open(file_name, 'r', encoding='UTF-8').readlines()
    map_set = [''] * 4986
    for line in lines:
        string_id = line.split("\t")
        # print("%d --- %s" % (int(string_id[1]), string_id[0]))
        map_set[int(string_id[1])] = string_id[0]
    herb_set = []
    sym_set = []
    for sym, herb in zip(sym_id, herb_id):
        syms = sym.split(" ")
        herbs = herb.split(" ")
        s_set = ''
        h_set = ''
        for s in syms:
            s_set += map_set[int(s)] + " "
        s_set += '\n'
        sym_set.append(s_set)
        for h in herbs:
            h_set += map_set[int(h)] + " "
        h_set += '\n'
        herb_set.append(h_set)

    file_sym = open(file_path + r'\symps_test_og.txt', 'w', encoding='UTF-8')
    file_herb = open(file_path + r'\herbs_test_og.txt', 'w', encoding='UTF-8')
    for ss, hs in zip(sym_set, herb_set):
        file_sym.write(ss)
        file_herb.write(hs)
        # print(" sym : %s --- herb : %s" %(sh, hs))


    # # #将分类好的数据集分开保存，herbPair-40 train and test
    # file = open(file_path + 'sym_only.txt', 'w')
    # for f_train in sym_set:
    #     file.write(f_train)
    # file.close()
    # file = open(file_path + 'herb_only.txt', 'w')
    # for f_test in herb_set:
    #     file.write(f_test)
    # file.close()


if __name__ == '__main__':
    write_file_path = r'D:\My project\pro_test_01\oriData'
    herb_link_file = r'D:\My project\pro_test_01\oriData\valid_5%.txt'
    map_entity_path = r'D:\My project\pro_test_01\oriData\entity_mapping.txt'
    sym_id, herb_id = dataSplit(herb_link_file)
    dataMap(map_entity_path, write_file_path, sym_id, herb_id)