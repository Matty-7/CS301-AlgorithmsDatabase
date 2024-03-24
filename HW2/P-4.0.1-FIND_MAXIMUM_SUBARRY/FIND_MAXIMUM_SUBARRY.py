# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 

import math
import tabulate
from Stats import Stats

indent  = -2

def brute_force(arr):
    # Complete the code here, see README on course website for problem description and instructions.
    max_sum = -float('inf')
    max_subarray = []
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                max_subarray = arr[i:j+1]
    return max_subarray

def FIND_MAXIMUM_SUBARRAY(A, low, high):

    global indent
    indent +=2

    # Complete the code here, see README on course website for problem description and instructions.
    #print("deepth is "+str(indent//2))
    if high-low==0:
        indent-=2
        return A  
    B = C = D = []
    mid=(low+high)//2
    print()
    print(Stats.PrintArrayRange(A, low, high) + ' %s   FIND_MAXIMUM_SUBARRAY [%s:%s] '% (' '*indent, low, high))
    if high-low==1:
        print(Stats.PrintArrayRange(A, low, high,[low]) + ' %s   base-case return %s '% (' '*indent, A[low]))
        
    B=FIND_MAXIMUM_SUBARRAY(A,low,mid)
    if mid+1==high and high-low>=2:
        print()
        print(Stats.PrintArrayRange(A, mid+1, high) + ' %s   FIND_MAXIMUM_SUBARRAY [%s:%s] '% (' '*(indent+2), mid+1, high))
    
    C=FIND_MAXIMUM_SUBARRAY(A,mid+1,high)
    D=FIND_MAX_CROSS_SUBARRAY(A,low,mid,high) 
    sumb=sum(B)
    sumc=sum(C)
    sumd=sum(D)
    if max(sumb,sumc,sumd)==sumb:
        if high-low>=2:
            index_l=A.index(B[0])
            index_r=A.index(B[len(B)-1])+1
            print(Stats.PrintArrayRange(A, low, high,[i for i in range(index_l,index_r)]) + ' %s   return %s -- FIND_MAXIMUM_SUBARRAY [%s:%s] '% (' '*(indent+2), sumb,low,high))
        indent-=2
        return B
    elif max(sumb,sumc,sumd)==sumc:
        if high-low>=2:
            index_l=A.index(C[0])
            index_r=A.index(C[len(C)-1])+1
            print(Stats.PrintArrayRange(A, low, high,[i for i in range(index_l,index_r)]) + ' %s   return %s -- FIND_MAXIMUM_SUBARRAY [%s:%s] '% (' '*(indent+2), sumc,low,high))
        indent-=2
        return C
    else:
        if high-low>=2:
            index_l=A.index(D[0])
            index_r=A.index(D[len(D)-1])+1
            print(Stats.PrintArrayRange(A, low, high,[i for i in range(index_l,index_r)]) + ' %s   return %s -- FIND_MAXIMUM_SUBARRAY [%s:%s] '% (' '*(indent+2), sumd,low,high))
        indent-=2
        return D    
    
def FIND_MAX_CROSS_SUBARRAY(A, low, mid, high): # must cross mid  
    if high - low != 1:
        print(Stats.PrintArrayRange(A, low, high, [mid]) + ' %s   FIND_MAX_CROSS_SUBARRAY %s %s %s '% (' '*(indent+2), low, high, mid))
    # Complete the code here, see README on course website for problem description and instructions.
    current1 = current2 = 0
    max1 = max2 = -math.inf
    B = C = []
    first1 = last1 = 0
    for i in range(mid,low-1,-1):
        current1+=A[i]
        if current1>max1:
            max1=current1
            B=A[i:mid]
            first1=i
    for j in range(mid,high):
        current2+=A[j]
        if current2>max2:
            max2=current2
            C=A[mid:j+1]
            last1=j
    D=B+C
    if high-low!=1:
        print(Stats.PrintArrayRange(A, first1, last1+1, [i for i in range(first1,last1+1)],symbol='x') + ' %s   FIND_MAX_CROSS_SUBARRAY return %s  '% (' '*(indent+2), sum(D)))
    return D

def transform(arr):
    return [arr[i+1]-arr[i] for i in range(len(arr)-1)]

def dash(msg, n=60):
    print()
    print('-'*n)
    print(msg)
    print('-'*n)
    pass

def main(A):
    dash('Original array')

    print(Stats.PrintArrayRange(A, 0, len(A)))

    Stats.Reset()
    dash('After transformation')
    B = transform(A)

    print(Stats.PrintArrayRange(B, 0, len(B)))


    dash('Solving for maximum subarray')
    u = FIND_MAXIMUM_SUBARRAY(B, 0, len(B))
    

    return u
    
if __name__ == '__main__':


    A='100 113 110 85 105 102 86 63 81 101 94 106 101 79 94 90 97'.split()
    #A=' 18    1   13   15   18    0    6   14   15    8 '.split()
    
    A=list(map(int, A))
    B = transform(A)
    
    a = main(A)

    dash('Divide and conquer result')
    print(a)
    b = brute_force(B)
    dash('Brutforce result')
    print(b)

    assert (b==a)