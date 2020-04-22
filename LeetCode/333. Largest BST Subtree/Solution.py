# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        # Time and Space Complexity: O(n)

        if root is None:
            return 0

        self.candidates = {}
        self.dfs(root)

        return max([self.candidates[node][2] for node in self.candidates])

    def dfs(self, node: TreeNode):
        isBst = True
        size = 1
        lower = node.val
        upper = node.val

        if node.left is not None:
            self.dfs(node.left)
            isBst = isBst and node.left in self.candidates and self.candidates[node.left][1] < node.val
            if isBst:
                size += self.candidates[node.left][2]
                lower = self.candidates[node.left][0]


        if node.right is not None:
            self.dfs(node.right)
            isBst = isBst and node.right in self.candidates and self.candidates[node.right][0] > node.val

            if isBst:
                size += self.candidates[node.right][2]
                upper = self.candidates[node.right][1]

        if isBst:
            self.candidates[node] = (lower, upper, size)
