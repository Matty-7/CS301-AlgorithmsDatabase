import math, Stats

# Hint: 
#
#    Can use the following fmt_num and PrintPartArray function to
#    instrument MERGE_SORT

def fmt_num(n): return '%3s' % str(n)

def PrintPartArray(A, p, q, tag=''  ):
    r = [''] * p + A[p:q] + ['']* (len(A) -q)
    r =  ' '.join(map(fmt_num, r)) + '    ' + tag
    print(r)
    return r

def MERGE(A, p, q, r):
        
    # MERGE(A[p:q] with A[q:r]

    # Complete the code here, see README on course website for problem description and instructions.
    n1 = q - p
    n2 = r - q
    L = A[p:q] + [math.inf]
    R = A[q:r] + [math.inf]

    i = j = 0
    for k in range(p, r):
        if i < n1 and (j >= n2 or L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            if R[j] == math.inf:
                Stats.Inc('r_inf_move_cnt')
            A[k] = R[j]
            j += 1

        if k == r - 1:
            PrintPartArray(A, p, k+1, 'L+R')

    return A


def MERGE_SORT(A, p, r):

    # Note: we are following Python list index semantics

    # Sort subarray A[p:r]
    # e.g. to sort A[:] use MERGE_SORT(A, 0, len(A))

    # Complete the code here, see README on course website for problem description and instructions.

    if p < r - 1:
        q = (p + r) // 2
        MERGE_SORT(A, p, q)
        MERGE_SORT(A, q, r)
        MERGE(A, p, q, r)

    return A



#-------------------------------------------
# Don't change code below this line
#-------------------------------------------
def main(A):
    Stats.PrintArray(A)
    MERGE_SORT(A, 0, len(A))
    Stats.PrintArray(A)
    n = len(A)
    Stats.Set (' %s*log_2(%s)'%(n,n), n*(math.log2(n)))
    Stats.PrintStats()
    return A
if __name__ == '__main__':

    A = [5,2,4,7,1,3,2,6 ] 


    main(A)

