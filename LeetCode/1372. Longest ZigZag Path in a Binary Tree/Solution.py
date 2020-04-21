# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.dp = {}
        self.dfs(root)

        result = 0
        for node in self.dp:
            result = max(result, self.dp[node][0], self.dp[node][1])

        return result - 1

    def dfs(self, node: TreeNode):
        left = 1
        right = 1

        if node.left is not None:
            self.dfs(node.left)
            left += self.dp[node.left][1]

        if node.right is not None:
            self.dfs(node.right)
            right += self.dp[node.right][0]

        self.dp[node] = (left, right)
