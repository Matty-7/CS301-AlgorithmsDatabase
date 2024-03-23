import tabulate
import Stats

def INSERTION_SORT(A):
    # Complete the code here, see README on course website for problem description and instructions.
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        Stats.Inc("cmpcnt")
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            Stats.Inc("swapcnt")
            i -= 1
            Stats.Inc('cmpcnt')
        A[i + 1] = key
        
    return A

def main(A):
    Stats.Reset()
    Stats.PrintArray(A, "input ")
    A = INSERTION_SORT(A)
    Stats.PrintArray(A, "sorted")
    Stats.PrintStats()
    return A
if __name__ == '__main__':

    A = [5,2,4,6,1,3]
    
    main(A)
    

    