# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not (root.left or root.right):
            return targetSum == root.val

        remain = targetSum - root.val
        return (root.left and self.hasPathSum(root.left, remain)) or (root.right and self.hasPathSum(root.right, remain))
