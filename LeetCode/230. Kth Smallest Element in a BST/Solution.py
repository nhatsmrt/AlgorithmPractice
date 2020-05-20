# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Tuple

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Time and Space Complexity: O(H + k)
        return self.find(root, k)[0]

    def find(self, node: TreeNode, target: int) -> Tuple[int, int]:
        if node == None:
            return -1, target

        val, target = self.find(node.left, target)

        if val != -1:
            return val, target

        if target == 1:
            return node.val, target

        return self.find(node.right, target - 1)

        
