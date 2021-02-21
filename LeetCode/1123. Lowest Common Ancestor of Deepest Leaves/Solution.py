# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Tuple


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # Time and Space Complexity: O(N)
        return self.dfs(root, 0)[0]

    def dfs(self, node: TreeNode, level: int) -> Tuple[TreeNode, int]:
        if not (node.left or node.right):
            # leaf
            return (node, level)
        elif not node.right:
            return self.dfs(node.left, level + 1)
        elif not node.left:
            return self.dfs(node.right, level + 1)
        else:
            left_lca, left_level = self.dfs(node.left, level + 1)
            right_lca, right_level = self.dfs(node.right, level + 1)

            if left_level < right_level:
                return right_lca, right_level
            elif right_level < left_level:
                return left_lca, left_level
            else:
                # node is the new lca of deepest leaves:
                return node, left_level
