# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(H)

        return self.compute(root, None, None)

    def compute(self, node: TreeNode, par: TreeNode, grand_par: TreeNode):
        if not node:
            return 0

        ret = self.compute(node.left, node, par) + self.compute(node.right, node, par)

        if grand_par and grand_par.val % 2 == 0:
            ret += node.val

        return ret
