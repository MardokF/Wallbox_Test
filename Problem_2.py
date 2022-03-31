# SPECIFICATIONS:

# INPUT : Give path of file systems

# OUTPUT : Find first file that satisfy:
#          1) The file owner is admin
#          2) The file is executable
#          1) The file size is lower than 14*2^20

import os
import pytest


#FILL THE PATH WITH EXISTING FOLDER IN YOUR PC
perc1 = 'C:/Users/marco/Downloads/Problem2_1'
perc2 = 'C:/Users/marco/Downloads/Problem2_2'
perc3 = 'C:/Users/marco/Downloads/Problem2_3'


file_spec = {
    'owner': 0,
    'ext': '.exe',
    'size': 14 * pow(2, 20)
}


def find_file(path, spec):
    fl = 0
    dir_list = os.listdir(path)
    for i in range(0, len(dir_list)):
        temp = path + '/' + dir_list[i]
        info = os.stat(temp)
        own = info.st_uid
        name, ext = os.path.splitext(temp)
        size = info.st_size
        if spec['owner'] == own and spec['ext'] == ext and spec['size'] > size:
            print(dir_list[i], ' satisfies the requirements.')
            fl = 1
            break
    return fl


if __name__ == '__main__':
    flag = find_file(perc1, file_spec)
    if not flag:
        print('Files do not satisfy requirements.')


    # Test_case1 : choose a directory with a file that meet specifications

def test_case1():
    flag1 = find_file(perc1, file_spec, flag)
    assert flag1 == 1


    # Test_case2 : choose a directory with no .exe files

def test_case2():
    flag2 = find_file(perc2, file_spec, flag)
    assert flag2 == 0


    # Test_case3 : choose a directory with .exe that don't meet specification

def test_case3():
    flag3 = find_file(perc3, file_spec, flag)
    assert flag3 == 0
