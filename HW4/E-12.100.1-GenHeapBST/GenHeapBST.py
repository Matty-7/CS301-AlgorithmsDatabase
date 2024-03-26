# Created by Jiang Long 
# 
# DKU CS301 FALL 2021 SESSION 01
# 

import drawtree
import math, random

def GenHeapBST (A):

    # Note: return an list of numbers which is either pre-order or BFS
    # order of the BST (Demo uses pre-order)

    # Complete the code here, see README on course website for problem description and instructions.

    A.sort()

    def build_heap_bst(nums, start, end):

        """
        Recursively constructs the Heap-BST from the sorted list of numbers.

        Args:
        nums (list): Sorted list of numbers.
        start (int): Starting index of the current segment of the list.
        end (int): Ending index of the current segment of the list.

        Returns:
        TreeNode: The root node of the constructed Heap-BST segment.
        """

        if start > end:
            return None

        num_nodes = end - start + 1

        height = int(math.log2(num_nodes))

        max_last_level = 2 ** height

        last_level_nodes = min(num_nodes - (2**height - 1), max_last_level)
        left_subtree_nodes = (2**height - 1) // 2 + min(max_last_level // 2, last_level_nodes)

        root_index = start + left_subtree_nodes

        root = drawtree.TreeNode(nums[root_index])
        root.left = build_heap_bst(nums, start, root_index - 1)
        root.right = build_heap_bst(nums, root_index + 1, end)

        return root

    def preorder_traversal(node):
        """
        Performs preorder traversal of the BST.

        Args:
        node (TreeNode): The current node in the traversal.

        Returns:
        list: The list of nodes in preorder traversal.
        """
        if node is None:
            return []
        return [node.val] + preorder_traversal(node.left) + preorder_traversal(node.right)

    root = build_heap_bst(A, 0, len(A) - 1)

    return preorder_traversal(root)


#-----------------------------------------------------
# Don't modify below this line
#-----------------------------------------------------
def main(A):
    r = GenHeapBST(A)
    print('BST preorder:', r)
    print()
    drawtree.draw_bst(r)
    # Note: usage of draw_bst
    # nums = [55, 30, 10, 5, 2, 20, 15, 25, 40, 35, 70, 60, 80, 75, 95]
    # draw_bst(nums)
    
    pass
    
if __name__ == '__main__':
    a = list(range(22))
    random.shuffle(a)
    main(a)

    pass
    
    

    