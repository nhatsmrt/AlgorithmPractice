# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ranges = {}
        self.dfs(root)

        ret = 0
        for node in self.ranges:
            ret = max(ret, abs(node.val - self.ranges[node][0]), abs(node.val - self.ranges[node][1]))

        return ret

    def dfs(self, node: TreeNode):
        min_range = node.val
        max_range = node.val

        if node.left is not None:
            self.dfs(node.left)
            min_range = min(min_range, self.ranges[node.left][0])
            max_range = max(max_range, self.ranges[node.left][1])

        if node.right is not None:
            self.dfs(node.right)
            min_range = min(min_range, self.ranges[node.right][0])
            max_range = max(max_range, self.ranges[node.right][1])


        self.ranges[node] = (min_range, max_range)
