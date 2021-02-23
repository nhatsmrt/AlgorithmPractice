# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(H)

        return self.dfs(root, -10000000000)

    def dfs(self, node: int, max_so_far) -> int:
        if not node:
            return 0

        ret = 1 if node.val >= max_so_far else 0
        max_so_far = max(node.val, max_so_far)
        ret += self.dfs(node.left, max_so_far) + self.dfs(node.right, max_so_far)

        return ret
