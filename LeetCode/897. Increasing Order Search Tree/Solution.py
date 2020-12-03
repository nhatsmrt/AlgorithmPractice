# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[0]

    def dfs(self, node):
        if not node:
            return None, None

        left_first, left_last = self.dfs(node.left)
        right_first, right_last = self.dfs(node.right)
        node.left, node.right = None, None


        if left_first and right_first:
            left_last.right = node
            node.right = right_first

            return left_first, right_last
        elif right_first:
            node.right = right_first
            return node, right_last
        elif left_first:
            left_last.right = node
            return left_first, node
        else:
            return node, node
