# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Time Complexity: O(N)

        if not (root1 and root2):
            return not (root1 or root2)

        if root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
