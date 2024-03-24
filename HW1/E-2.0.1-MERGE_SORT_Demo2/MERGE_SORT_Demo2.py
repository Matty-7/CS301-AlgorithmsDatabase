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
    """
    Merges two sorted sub-arrays of A into a single sorted array.

    The first sub-array is A[p:q], and the second sub-array is A[q:r].
    Uses sentinel values to simplify merging logic.

    Args:
        A (list): The target list to be sorted.
        p (int): Starting index of the first sub-array.
        q (int): Ending index of the first sub-array and starting index of the second sub-array.
        r (int): Ending index of the second sub-array.

    Returns:
        None: Sorts the array in-place.
    """
    
    n1 = q - p
    n2 = r - q
    L = [0] * n1 + [float('inf')]
    R = [0] * n2 + [float('inf')]

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j]
    
    #L.append(float('inf'))
    #R.append(float('inf'))

    i = j = 0
    B = []

    if len(L) == len(A) // 2 + 1:
        B.extend(L[:-1])
        B.extend(R[:-1])

    for k in range(p, r):
        if L[i] != float('inf') and R[j] != float('inf'):
            if L[i] <= R[j]:
                Stats.Inc('cmpcnt')
                if len(L) == len(A) // 2 + 1:
                    index1 = B.index(L[i])
                    B[index1] = "*"
                    PrintPartArray(B, p, r, tag=f'k={k} L+R')
                    B[index1] = "-"
                    A[k] = L[i]
                    PrintPartArray(A, p, k+1, tag='A')
                    print()
                else:
                    A[k] = L[i]
                i += 1
            else:
                if len(L) == len(A) // 2 + 1:
                    index2 = B.index(R[j])
                    B[index2] = "*"
                    PrintPartArray(B, p, r, tag=f'k={k} L+R')
                    B[index2] = "-"
                    A[k] = R[j]
                    PrintPartArray(A, p, k+1, tag='A')
                    print()
                else:
                    A[k] = R[j]
                j += 1
                Stats.Inc('cmpcnt')
        elif L[i] == float('inf'):
            Stats.Inc('cmpcnt')
            if len(L) == len(A) // 2 + 1:
                index3 = B.index(R[j])
                B[index3] = "*"
                PrintPartArray(B, p, r, tag=f'k={k} L+R')
                B[index3] = "-"
                A[k] = R[j]
                PrintPartArray(A, p, k+1, tag='A')
                print()
            else:
                A[k] = R[j]
            j += 1
        else:
            Stats.Inc('r_inf_move_cnt')
            Stats.Inc('cmpcnt')
            if len(L) == len(A) // 2 + 1:
                index4 = B.index(L[i])
                B[index4] = "*"
                PrintPartArray(B, p, r, tag=f'k={k} L+R')
                B[index4] = "-"
                A[k] = L[i]
                PrintPartArray(A, p, k+1, tag='A')
                print()
            else:
                A[k] = L[i]
            i += 1


def MERGE_SORT(A, p, r):

    # Note: we are following Python list index semantics


    # Sort subarray A[p:r]
    # e.g. to sort A[:] use MERGE_SORT(A, 0, len(A))

    # Complete the code here, see README on course website for problem description and instructions.

    if p < r - 1:
        q = (p + r) // 2
        MERGE_SORT(A,p,q)  
        MERGE_SORT(A,q,r)
        MERGE(A,p,q,r)


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

