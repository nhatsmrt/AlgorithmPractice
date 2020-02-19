# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff = abs(root.val - target)
        if root.val == target:
            return root.val
        elif root.val < target:
            if root.right is None:
                return root.val
            candidate = self.closestValue(root.right, target)
            candidate_diff = abs(candidate - target)
            return root.val if diff < candidate_diff else candidate
        else:
            if root.left is None:
                return root.val
            candidate = self.closestValue(root.left, target)
            candidate_diff = abs(candidate - target)
            return root.val if diff < candidate_diff else candidate

            
