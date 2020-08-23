# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_leaf(node):
    return node and not (node.left or node.right)

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = []
        leaves2 = []

        self.get_leaf(root1, leaves1)
        self.get_leaf(root2, leaves2)

        return leaves1 == leaves2

    def get_leaf(self, node: TreeNode, ret: List[int]):
        if is_leaf(node):
            ret.append(node.val)
        elif node:
            self.get_leaf(node.left, ret)
            self.get_leaf(node.right, ret)
        
