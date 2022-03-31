# SPECIFICATIONS:

# INPUT : Give two arrays of integers

# OUTPUT : Find if there is a repetition

import pytest

a = [1, 2, 3, 4]
b = [5, 9, 'a']


def control(vect1, vect2):
    fl = 0
    n_rep = []
    for i in range(0, len(vect2)):

        if not isinstance(vect1[i], int) or not isinstance(vect2[i], int):
            print('Vector must contain integer variable')
            fl = 1
        else:
            if vect2[i] in vect1:
                print('First repetition', vect2[i])
                n_rep = vect2[i]
                break
    return fl, n_rep


if __name__ == '__main__':
    flag, n_rep = control(a, b)
    if not n_rep:
        print('No repetition')


# Test_case1 : Compare Two integers array with Repetition

def test_case1():
    a_t1 = [1, 2, 3, 4]
    b_t1 = [5, 6, 7, 4, 8, 9]
    flag1, n_rep1 = control(a_t1, b_t1)
    assert flag1 == 0 and n_rep1 == 4

# Test_case2 : Compare Two integers array with Repetition

def test_case2():
    a_t2 = [1, 2, 3, 4]
    b_t2 = [5, 'b', 7, 2, 8, 9]
    flag2, n_rep2 = control(a_t2, b_t2)
    assert flag2 == 1 and n_rep2 == 2

# Test_case3 : Compare Two integers array without Repetition

def test_case3():
    a_t3 = [1, 2, 3, 4]
    b_t3 = [8, 9, 10]
    flag3, n_rep3 = control(a_t3, b_t3)
    assert flag3 == 0 and n_rep3 == []
