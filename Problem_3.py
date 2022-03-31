# SPECIFICATIONS:

# INPUT : Give two different arrays of the same length with sequence of Coin Flip (0,1)

# OUTPUT : Count the changes needed to have two equal arrays

import pytest

comb1 = [0, 1, 1, 0]
comb2 = [0, 1, 0, 1]
comb3 = [0]
comb4 = ['a', 1, 0, 0]


def perm(a, b):
    counter = 0
    err = 0
    try:
        for i in range(0, len(a)):
            if 0 <= a[i] <= 1 and 0 <= b[i] <= 1:
                if not a[i] == b[i]:
                    counter += 1
        print('Permutations needed = ', counter)
    except:
        print('Check that arrays have same length or values are different from 0,1')
        err = 1
    return counter, err


if __name__ == '__main__':
    perm(comb1, comb4)


# Test_case1 : Compare two arrays of same length and with at least one different coin flip result

def test_case1():
    counter1, err1 = perm(comb1, comb2)
    assert counter1 > 0 and err1 == 0


# Test_case2 : Compare two equal arrays

def test_case2():
    counter2, err2 = perm(comb1, comb1)
    assert counter2 == 0 and err2 == 0


# Test_case3 : Compare two arrays with different length

def test_case3():
    counter3, err3 = perm(comb1, comb3)
    assert counter3 == 0 and err3 == 1

# Test_case4 : Compare two arrays with different length

def test_case4():
    counter4, err4 = perm(comb1, comb4)
    assert counter4 == 0 and err4 == 1
