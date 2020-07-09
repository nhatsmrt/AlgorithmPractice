# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # Time and Space Complexity: O(N)
        self.levels = {}
        self.dfs(root, 0, 0)

        ret = 0
        for level in self.levels:
            ret = max(ret, self.levels[level][1] - self.levels[level][0] + 1)

        return ret

    def dfs(self, node: TreeNode, level: int, code: int) -> int:
        if level not in self.levels:
            self.levels[level] = [code, code]

        self.levels[level][0] = min(code, self.levels[level][0])
        self.levels[level][1] = max(code, self.levels[level][1])

        if node.left is not None:
            self.dfs(node.left, level + 1, code * 2)

        if node.right is not None:
            self.dfs(node.right, level + 1, code * 2 + 1)
