# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Time and Space Complexity: O(n)
        return self.dfs(root, sum, 0, {0: 1})

    def dfs(self, node: TreeNode, target: int, prefix: int, prefixes):
        ret = 0

        if node is not None:
            prefix += node.val
            ret += prefixes.get(prefix - target, 0)
            prefixes[prefix] = prefixes.get(prefix, 0) + 1

            ret += self.dfs(node.left, target, prefix, prefixes) + self.dfs(node.right, target, prefix, prefixes)
            prefixes[prefix] -= 1

        return ret
