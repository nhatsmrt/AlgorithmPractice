# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(H)

        return self.dfs(root, Counter())

    def dfs(self, node: TreeNode, cnter: Counter) -> int:
        if node:
            cnter[node.val] += 1

            if node.left or node.right:
                ret = self.dfs(node.left, cnter) + self.dfs(node.right, cnter)
            else:
                num_odd = 0
                for val in cnter:
                    if cnter[val] % 2 == 1:
                        num_odd += 1


                ret = 1 if num_odd <= 1 else 0

            cnter[node.val] -= 1
            return ret
        else:
            return 0
