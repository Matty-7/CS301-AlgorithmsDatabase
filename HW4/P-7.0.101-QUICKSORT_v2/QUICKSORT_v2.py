# 
# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 

import random


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        assert left is None or isinstance(left, TreeNode)
        assert right is None or isinstance(right, TreeNode)
        self.left = left
        self.right = right
        pass
    
    def inorder(self):

        # return as a sorted list
        # Complete the code here, see README on course website for problem description and instructions.

        res = []
        stack = []
        cur = self

        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res

def PARTITION(A):
    
    # Use A[-1] as pivot and do a simple partition by filtering left to right

    # Complete the code here, see README on course website for problem description and instructions.

    r = len(A)
    x = A[-1]
    a = [i for i in A[:r-1] if i <= x]
    b = [i for i in A[:r-1] if i > x]

    # a is a list, x is an int val, b is a list, see demo
    print("Partition: " , A, ' to {', a, x, b, '}')

    return a,x,b
    

def QUICKSORT(A):

    # return TreeNode: the sorted order as a binary tree

    # Complete the code here, see README on course website for problem description and instructions.

    if len(A) == 0:
        return None
    
    if len(A) == 1:
        return TreeNode(A[0])
    
    x = A[-1]
    a,x,b = PARTITION(A)
    return TreeNode(x, QUICKSORT(a), QUICKSORT(b))

#-----------------------------------------------------
# Don't modify below this line
#-----------------------------------------------------

def main(A):
    global show_detail
    print('input:', A)
    t = QUICKSORT(A)
    B = t.inorder()
    print('result:', B)
    assert B == list(sorted(A))
    return t

if __name__=='__main__':
    random.seed(1)
    A = list(range(10))
    random.shuffle(A)
    A = [2,8,7,1,3,5,6,4]
    main(A)
    pass