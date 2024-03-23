import tabulate
import Stats

def INSERTION_SORT(A):
    # Complete the code here, see README on course website for problem description and instructions.




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
    

    