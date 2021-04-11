# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(H)
        return self.sum_with_height(root, 0)[1]

    def sum_with_height(self, node: TreeNode, height: int) -> int:
        if not (node.left or node.right):
            return (height, node.val)

        if not node.left:
            return self.sum_with_height(node.right, height + 1)

        if not node.right:
            return self.sum_with_height(node.left, height + 1)

        leftheight, leftsum = self.sum_with_height(node.left, height + 1)
        rightheight, rightsum = self.sum_with_height(node.right, height + 1)

        if leftheight == rightheight:
            return (leftheight, leftsum + rightsum)
        else:
            return max([(leftheight, leftsum), (rightheight, rightsum)])
