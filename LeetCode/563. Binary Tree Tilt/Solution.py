# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        return self.dfs(root)[0]

    def dfs(self, node: TreeNode):
        if not node:
            return 0, 0

        left_tilt, left_sum = self.dfs(node.left)
        right_tilt, right_sum = self.dfs(node.right)

        return (left_tilt + right_tilt + abs(left_sum - right_sum), left_sum + right_sum + node.val)
