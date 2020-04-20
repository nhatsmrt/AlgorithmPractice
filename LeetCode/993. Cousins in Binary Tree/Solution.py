# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level1, par1 = self.find_level(root, None, x)
        level2, par2 = self.find_level(root, None, y)

        return level1 == level2 and par1 != par2

    def find_level(self, node: TreeNode, par: TreeNode, val: int):
        if node is not None:
            if node.val == val:
                return 0, par

            candidate, par = self.find_level(node.left, node, val)
            if candidate != -1:
                return 1 + candidate, par

            candidate, par = self.find_level(node.right, node, val)
            if candidate != -1:
                return 1 + candidate, par


        return -1, None
        
