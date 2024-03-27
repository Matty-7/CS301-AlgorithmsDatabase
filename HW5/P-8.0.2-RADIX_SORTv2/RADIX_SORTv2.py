#
# Created by Jiang Long 
#
# DKU CS301 FALL 2021 SESSION 02
#

import Stats, math, random

def RADIX_SORT(A, r, d):
    # d: number of digits
    # r: radix in number of r binary bits
    
    Stats.PrintArray(A, 'RADIX_SORT(A, 2^%d, %d)'% (r,d))
    
    # In each iteration of the COUNTING_SORT_on_radix, you should use
    # the following to print out the Array after the re-arrangement:
    
    # for i in range(d): 
    #    .... call COUNTING_SORT_on_radix
    #    Stats.PrintArray(A, 'iter %s'%i)
    
    # Complete the code here, see README on course website for problem description and instructions.

    for i in range(d):
        A = COUNTING_SORT_on_radix(A, r, i)
        Stats.PrintArray(A, 'iter %s'%i)

    return A


def COUNTING_SORT_on_radix(A, r, i_th):

    # r is the number of binary bits in the radix
    # i_th `digit`
    # return array B which is sorted on the i_th 'digit' base on radix 2^r

    # Complete the code here, see README on course website for problem description and instructions.

    B = A.copy()
    C = A.copy()
    for j in range(len(A)):
        C[j] = (A[j] >> (r * i_th)) & (2**r - 1)

    for i in range(len(A)):
        key = C[i]
        val = B[i]
        j = i - 1
        while j >= 0 and C[j] > key:
            C[j + 1] = C[j]
            B[j + 1] = B[j]
            j -= 1
        C[j + 1] = key
        B[j + 1] = val

    return B

#-------------------------------------------
# Don't modify below this line
#-------------------------------------------
def main(A, r=4, d=3):
    
    # The default is radix 16 and total 3 hex digits

    Stats.Reset()
    n = len(A)

    B = RADIX_SORT(A, r, d)
    assert(list(sorted(B))==B)
    Stats.PrintArray(B, 'SORTED A')
    
    pass


if __name__=='__main__':
    A = [2,3,5,0,2,3,0,3]

    random.seed(len(A))
    A = [ int(random.uniform(512, 4096)) for i in range(10)]
    A = [329, 457,657, 839,436,720, 355]
    main(A)
    pass