# 
# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 

import os, math, random, Stats

#------------------------------------------------
# Feel free to introduce helper functions.
#------------------------------------------------

def PARTITION(A, p, r):
    # copy this from your earlier JPA
    # Complete the code here, see README on course website for problem description and instructions.
    value = A[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if A[j] <= value:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i + 1], A[r - 1] = A[r - 1], A[i + 1]
    return i + 1

def PARTITION_modified(A, p, r, x):
    
    # We know is the value of the pivot var, but we don't know where
    # it is, this for loop is to find its occurrence searching from
    # left to right of the list, and then call PARTITION
    
    # Complete the code here, see README on course website for problem description and instructions.
    for i in range(p, r):
        if A[i] == x:
            A[r-1], A[i] = A[i], A[r-1]
    return PARTITION(A, p, r)

def SELECT(A, p, r, ith, deep=0):
    # Note: the semantics is to return x = sorted(A)[ith]
    global LEN
    global recur_depth
    recur_depth=deep
    print(' ' * deep * 2, 'SELECT( %s, %s)' % (A[p:r], ith))

    # select the i_th from [p..r) , excluding position q
    # i starts with 0
    if r - p <= 5:
        assert ith < 5
        sx = list(sorted(A[p:r]))
        recur_depth -= 1
        return sx[ith]

    # Complete the code here, see README on course website for problem description and instructions.
    C = []
    for i in range(p, r, 5):
        if i + 5 > r:
            B = sorted(A[i:r])
        else:
            B = sorted(A[i:i + 5])
        C.append(B[len(B)// 2])
    half= len(C) // 2
    mid = SELECT(C, 0, len(C),half,deep+1)
    LEN = 0
    pivot_index= PARTITION_modified(A, p, r, mid) 
    check=pivot_index-p 
    if check == ith :
        return mid
    elif check > ith:
        return SELECT(A, p, pivot_index, ith,deep+1)
    else:
        return SELECT(A, pivot_index+1, r, ith-check-1,deep+1)
    
#--------------------------------------------------------------------
# Don't modify below this line
#--------------------------------------------------------------------
def main(A, i = None):
    global verbose
    verbose = len(A)< 20
    if i == None : i = len(A) //2 # pick the median

    Stats.Reset()
    n = len(A)
    Stats.Set('len(A)', n)
    Stats.Set('i', i)
    Stats.PrintArray(A, 'A (input)')
    
    B = SELECT(A, 0, len(A), i)


    Stats.Set('%s_{th} order-stats' % i, B)
    Stats.PrintStats()
    return B

#--------------------------------------------------------------------
# Ignore below, SAG judge execute SELECT.py from main.py
#--------------------------------------------------------------------
if __name__=='__main__':
    #A = [2,3,5,0,2,3,0,3]
    random.seed(0)
    A = list(range(22))
    random.shuffle(A)
    #A = [3, 1, 4, 2, 0, 5, 6, 9, 8, 7] 
    # A =  [1, 4, 3, 0, 2, 5, 6, 7, 8, 9, 10, 11, 19, 17, 20, 15, 13, 18, 12, 21, 14, 16] 
    # A =  [4, 5, 1, 6, 3, 0, 2, 7, 8, 9, 14, 10, 17, 21, 11, 19, 13, 12, 16, 20, 18, 15] 
    # A = [6, 7, 8, 3, 9, 1, 4, 2, 5, 0]
    main(A,9)
    for i in range(len(A)):
        #print('main', A, i)
        random.shuffle(A)
        main(A,i+len(A)//2)
        break