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




    pass


def MERGE_SORT(A, p, r):

    # Note: we are following Python list index semantics

    # Sort subarray A[p:r]
    # e.g. to sort A[:] use MERGE_SORT(A, 0, len(A))

    # Complete the code here, see README on course website for problem description and instructions.





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

