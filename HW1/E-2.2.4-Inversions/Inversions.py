import math
import tabulate
import Stats

def brute_inversion(A):
    # Complete the code here, see README on course website for problem description and instructions.
    cnt = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] > A[j]:
                cnt += 1
    return cnt

def MERGE(A, p, q, r):
    # MERGE(A[p:q] with A[q:r]

    # Complete the code here, see README on course website for problem description and instructions.

    n1 = q - p
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j]
    L.append(math.inf)
    R.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] != math.inf and R[j] != math.inf:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                Stats.Inc('inverse_cnt', n1 - i)
                A[k] = R[j]
                j += 1
        elif L[i] == math.inf:
            A[k] = R[j]
            j += 1
        else:
            Stats.Inc('r_inf_move_cnt')
            A[k] = L[i]
            i += 1
        
        
def MERGE_SORT(A, p, r):
    # sort subarray A[p:r]
    # e.g. to sort A[:] use MERGE_SORT(A, 0, len(A))

    # Complete the code here, see README on course website for problem description and instructions.
    q = (p + r) // 2
    if p < q:
        MERGE_SORT(A, p, q)
        MERGE_SORT(A, q, r)
        MERGE(A, p, q, r)



#-------------------------------------------
# Don't change code below this line
#-------------------------------------------
def main(A):
    Stats.PrintArray(A)
    Stats.Reset()
    Stats.Set('BruteForce_cnt', brute_inversion(A))
    MERGE_SORT(A, 0, len(A))
    n = len(A)
    Stats.PrintArray(A)
    Stats.PrintStats()

    return A
if __name__ == '__main__':

    A = [2,3,8,6,1]

#    A +=A

    main(A)