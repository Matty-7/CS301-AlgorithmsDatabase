#
# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 


import random
import random,  queue
import rIO, drawtree, Stats

class BST_Nil:
    def __init__(self):
        self.size = 0
        self.key = '#'
        self.left = None
        self.right = None
        pass
    def IsNil(self): return True
    def __str__(self): return '#'
    @property 
    def val(self): return 'nil'
    pass

nil = BST_Nil()

class BST_Node:
    def __init__(self, key):
        self.left = nil
        self.right = nil
        self.p = nil
        self.key = key
        
        pass
    def IsNil(self): return False
    def __str__(self): return str(self.key)
    @property 
    def val(self): return self.key
    pass

class BST_Tree:
    def __init__(self):
        self.root = nil
        pass

    # Note: You may need to add additional methods for recursion

    # Complete the code here, see README on course website for problem description and instructions.
    def inorder(self):
        if self.root != nil:
            self.out = []
            x = self.root
            self.inorder_tree_walk(x.left)
            self.out.append(self.root)
            self.inorder_tree_walk(x.right)
        return self.out

    def inorder_tree_walk(self, node):
        if node == nil:
            return
        assert isinstance(node, BST_Node)
        if node.IsNil:
            self.inorder_tree_walk(node.left)
            self.out.append(node)
            self.inorder_tree_walk(node.right)


    def preorder(self):
        if self.root != nil:
            self.out1 = []
            self.out1.append(self.root)
            self.iterative_tree_search(self.root.left)
            self.iterative_tree_search(self.root.right)
        return self.out1

    def iterative_tree_search(self, node):
        if node == nil:
            return
        assert isinstance(node, BST_Node)
        if node.IsNil:
            self.out1.append(node)
            self.iterative_tree_search(node.left)
            self.iterative_tree_search(node.right)

    def size(self):
        return len(self.preorder())

    def tree_insert(self, node):
        assert isinstance(node, BST_Node)
        y = nil
        x = self.root
        while x != nil:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.p = y  
        if y == nil:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def ith_element(self, ith):
        a = self.inorder()
        return (a[ith])

    def check(self):
        return True

    def DrawTree(self):
        if self.root.IsNil(): return 'nil'
        return drawtree.drawtree2(self.root)
    pass

#-----------------------------------------------------------
# Don't modify below this line
#-----------------------------------------------------------
def main(A):
    T =BST_Tree()
    random.seed(0)
    random.shuffle(A)
    rIO.dash("Input:")
    print(A)
    print()

    
    rIO.dash("Test TREE_INSERT: "+ str(A))
    for i in A:
        T.tree_insert(BST_Node(i))

    v = [i.key for i in T.inorder()]
    print('\nPost ALL INSERT Inorder: ', v)
    
    v = [i.key for i in T.preorder()]
    print('\nPost ALL INSERT Preorder: ', v)
    print()

    print(T.DrawTree())


    # Test DELETE and Ith

    r = T.size()
    for i in reversed(range(r)):
        

        ith = random.randint(0,i)

        # Get the ith elem and delete it 
        a = T.ith_element(ith)
        print("INFO: %d_th key in T: %s" % (ith, a.key))
        assert T.check()




if __name__=='__main__':
    A = list(range(20))
    
    main(A)