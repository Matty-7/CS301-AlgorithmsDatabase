import functools, operator, random, Stats, math, os
import rIO
import random
from MAX_HEAP import MAX_HEAP, PARENT, LEFT, RIGHT
import rIO

class PRIORITY_QUEUE(MAX_HEAP):
    
    def __init__(self, A=[], key = None):
        MAX_HEAP.__init__(self, A, key , verbosity = False)
        #if self.key == None: self.key = lambda i: i
        self.BUILD_MAX_HEAP()

    def HEAPSIZE(self): 
        return self.heapsize
    
    def INSERT(self,key):
        assert isinstance(key, int)
        
        # Note: here needs to extend A's length if heapsize>=len(A)
        
        # Complete the code here, see README on course website for problem description and instructions.

        if len(self.A) <= self.heapsize:
            self.A.append(-math.inf)
        else:
            self.A[self.heapsize] = -math.inf
        self.heapsize += 1
        self.INCREASE_KEY(self.heapsize-1, key)

    def MAXIMUM(self):
        # Complete the code here, see README on course website for problem description and instructions.
        return self.A[0]

    def EXTRACT_MAX(self):
        if self.HEAPSIZE()==0:
            return None

        r = self.A[0]
        
        # Complete the code here, see README on course website for problem description and instructions.
        self.A[0] = self.A[self.heapsize-1]
        self.A[self.heapsize-1] = r
        self.heapsize -= 1
        self.MAX_HEAPIFY(0)

        return r
    
    def INCREASE_KEY(self, i, k): # increase the key value for A[i]
        # error handling: ignore
        if i >= self.heapsize: return 
        # error handling: ignore
        if k< self.A[i] : return 

        # Complete the code here, see README on course website for problem description and instructions.

        self.A[i] = k
        while i > 0 and self.A[PARENT(i)] < self.A[i]:
            self.A[i], self.A[PARENT(i)] = self.A[PARENT(i)], self.A[i]
            i = PARENT(i)
    
#-------------------------------------------------------
# Test client : No need to change anything below this line
#-------------------------------------------------------
def main(A):
    # Create an empty queue
    p = PRIORITY_QUEUE()

    # Test INSERT method

    rIO.dash('Test INSERT: ')
    for i in A: 
        print('INSERT(%s)' % i)
        p.INSERT(i)
        pass
    print(p.DrawTree(None, False))

    # Test INCREASE_KEY method
    random.seed(sum(A))

    rIO.dash('Test INCREASE_KEY')
    for i in range(p.HEAPSIZE()//2):
        x = random.randint(1, p.HEAPSIZE()-1)
        old_key = p.A[x]
        new_key = int(p.A[x] * 1.5)
        print('INCREASE_KEY(A, %s, %s) [where A[%s] was %s] ' % (x, new_key, x, old_key))
        p.INCREASE_KEY(x, new_key)
        pass
    
    print(p.DrawTree(None, False))

    rIO.dash('Text EXTRACT_MAX')
    # Test EXTRACT_MAX method
    while p.HEAPSIZE() > 0:
        a = p.EXTRACT_MAX()
        print('EXTRACE_MAX:',a )
        pass

    pass

if __name__=='__main__':
    random.seed(0)
    A = list(range(10))
    random.shuffle(A)
    main(A)
    pass