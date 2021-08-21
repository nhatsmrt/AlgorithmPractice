# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        # Time and Space Complexity: O(N)

        return self.dfs(root)[1]

    def dfs(self, node: Optional[TreeNode]) -> tuple:
        if node is None:
            return (0, 0)

        left_sum, left_cnt = self.dfs(node.left)
        right_sum, right_cnt = self.dfs(node.right)

        ret_sum = node.val + left_sum + right_sum
        ret_cnt = left_cnt + right_cnt

        if node.val == left_sum + right_sum:
            ret_cnt += 1

        return ret_sum, ret_cnt
