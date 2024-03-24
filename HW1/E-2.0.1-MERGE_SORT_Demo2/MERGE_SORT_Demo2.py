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
    Merge two sorted sub-arrays of arr[] and use Stats.Inc for statistics
    and PrintPartArray for demonstrating the merging process.

    Args:
        arr (list): The target array to be sorted.
        left (int): Starting index of the first sub-array.
        mid (int): Ending index of the first sub-array and starting index of the second sub-array.
        right (int): Ending index of the second sub-array.

    Returns:
        None: The function modifies the array in-place.
    """
    

    n1 = q - p
    n2 = r - q   
    L = [0] * n1
    R = [0] * n2

    for n in range(n1):
        L[n] = A[p + n]
    for m in range(n2):
        R[m] = A[q + m]
    
    L.append(float('inf'))
    R.append(float('inf'))

    i = j = 0

    B = []

    if len(L) == len(A) // 2 + 1:
        for m in range(len(L) - 1):
            B.append(L[m])
        for n in range(len(R) - 1):
            B.append(R[n])

    for k in range(p,r):
        if L[i]!=math.inf and R[j]!=math.inf:
            if L[i]<=R[j]:
                Stats.Inc('cmpcnt')
                if(len(L)==len(A)//2+1):
                    index1=B.index(L[i])
                    B[index1]="*"
                    PrintPartArray(B,p,r,tag= 'k='+str(k)+' L+R' )
                    B[index1]="-"
                    A[k]=L[i]
                    PrintPartArray(A,p,k+1,tag='A')
                    print()
                else:A[k]=L[i]
                i+=1
            else:
                if(len(L)==len(A)//2+1):
                    index2=B.index(R[j])
                    B[index2]="*"
                    PrintPartArray(B,p,r,tag= 'k='+str(k)+' L+R' )
                    B[index2]="-"
                    A[k]=R[j]
                    PrintPartArray(A,p,k+1,tag='A')
                    print()
                else:A[k]=R[j]
                j+=1
                Stats.Inc('cmpcnt')
        elif L[i]==math.inf:
            Stats.Inc('cmpcnt')
            if(len(L)==len(A)//2+1):
                index3=B.index(R[j])
                B[index3]="*"
                PrintPartArray(B,p,r,tag= 'k='+str(k)+' L+R' )
                B[index3]="-"
                A[k]=R[j]
                PrintPartArray(A,p,k+1,tag='A')
                print()
            else:A[k]=R[j]
            j+=1
        else:
            Stats.Inc('r_inf_move_cnt')
            Stats.Inc('cmpcnt')
            if(len(L)==len(A)//2+1):
                index4=B.index(L[i])
                B[index4]="*"
                PrintPartArray(B,p,r,tag= 'k='+str(k)+' L+R' )
                B[index4]="-"
                A[k]=L[i]
                PrintPartArray(A,p,k+1,tag='A')
                print()
            else:A[k]=L[i]
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

