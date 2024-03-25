#
# Created by Jiang Long for CS301 DKU Fall 2021
#

import random, Stats, functools

import  drawtree, rIO

#-------------------------------------------------
# Note: The implementation should follow textbook closely
#-------------------------------------------------

def PARENT(i): 
    # Complete the code here, see README on course website for problem description and instructions.
    return (i-1)//2

def LEFT(i):  
    # Complete the code here, see README on course website for problem description and instructions.
    return 2*i+1

def RIGHT(i):  
    # Complete the code here, see README on course website for problem description and instructions.
    return 2*i+2

# MAX_HEAP inherit from build-in class list
class MAX_HEAP:
    # constructor
    def __init__(self, A=[], key = None, verbosity = True):
        self.A = A
        self.verbosity = verbosity # debug printing
        self.key = key
        if self.key is None : self.key = lambda i: i
        self.heapsize = len(A)
        self.recur_depth = 0
        self.BUILD_MAX_HEAP()
        
    def HEAPSIZE(self): return self.heapsize

    def BUILD_MAX_HEAP(self):
        if self.verbosity :
            rIO.dash("BUILD_MAX_HEAP: %s" %str(self.A))
        
        # Complete the code here, see README on course website for problem description and instructions.
        for i in range(PARENT(self.heapsize-1),-1,-1):
            self.MAX_HEAPIFY(i)

        assert self.Check_IsHEAP()
    
    def Check_IsHEAP(self):
        # Complete the code here, see README on course website for problem description and instructions.
        for i  in range(PARENT(self.heapsize-1)):
            L = LEFT(i)
            R = RIGHT(i)
            if L < self.heapsize and self.A[L] > self.A[i]:
                return False
            if R < self.heapsize and self.A[R] > self.A[i]:
                return False
            
        return True
    
    def MAX_HEAPIFY(self, i):   # use self.heapsize as the heapsize
        
        self.recur_depth +=1

        # move the larger ones to the leaf
        if self.verbosity :
            rIO.dash("MAX_HEAPIFY %s (recur_depth:%d)" % (i, self.recur_depth))
        
        # remember the current tree 
        before = self.DrawTree(i) # for use in print the tree/heap transformation

        # Coding Task
        #
        # 1. Implement MAX_HEAPIFY as in textbook
        #
        # 2. Use self.DrawTree and rIO.concat_text_block to visualize
        # the process (see README)
        #
        
        # Complete the code here, see README on course website for problem description and instructions.
        #B=self.A.copy()
        #B[i]='('+str(self.A[i])+')'
        L=LEFT(i)
        R=RIGHT(i)
        if L < self.heapsize and self.A[L]>self.A[i]:
            max=L
        else:
            max=i
        if R < self.heapsize and self.A[R]>self.A[max]:
            max=R
        if max!=i:
            temp=self.A[i]
            self.A[i]=self.A[max]
            self.A[max]=temp
            self.MAX_HEAPIFY(max)
        else:
            pass

        self.recur_depth=0

    def HEAP_SORT(self):
        rIO.dash("HEAP_SORT")
        # Complete the code here, see README on course website for problem description and instructions.
        while self.heapsize > 1:
            #swap
            temp = self.A[0]
            self.A[0] = self.A[self.heapsize-1]
            self.A[self.heapsize-1] = temp
            self.heapsize = self.heapsize - 1
            self.MAX_HEAPIFY(0)
    
    #-------------------------------------------------
    # To be used with rIO.concat_text_block(see README)
    #-------------------------------------------------
    def DrawTree(self, k=None, all = True):
        
        B = [i for i in  (self.A if all else self.A[:self.HEAPSIZE()]) ]
        if not k is None:
            B[k] = '(%s)'% B[k]
        r = drawtree.draw_level_order2(B)
        return r
    
#-------------------------------------------------
# No need to modify below this line
#-------------------------------------------------
def main(A):

    print("Input A:", A)

    h = MAX_HEAP(A)
    
    h.HEAP_SORT()

    rIO.dash("sorted A: %s" % A)
    
    assert A == list(sorted(A))

if __name__=='__main__':
    random.seed(0)
    A = list(range(10))
    random.shuffle(A)
    main(A)