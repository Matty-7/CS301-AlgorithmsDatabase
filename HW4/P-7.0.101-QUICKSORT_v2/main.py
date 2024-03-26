import sys, drawtree



import QUICKSORT_v2


                          
ax = sys.stdin.read().split()

# convert stdin to int array for input
A = [int(i) for i in ax]

# Get the tree
t = QUICKSORT_v2.main(A)

# get the ordered list
B = t.inorder()

# self-check
assert B == list(sorted(A))


print ('----------------------------')
print("Tree")
print ('----------------------------')

drawtree.drawtree(t)