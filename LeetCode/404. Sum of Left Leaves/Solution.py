# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def is_leaf(node):
    return not (node.left or node.right)

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.sum_leaves(root, False)

    def sum_leaves(self, node: TreeNode, is_left: bool) -> int:
        if node:
            if is_leaf(node):
                if is_left:
                    return node.val
            else:
                return self.sum_leaves(node.left, True) + self.sum_leaves(node.right, False)
        return 0

        
