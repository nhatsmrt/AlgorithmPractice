# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Tuple

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        # Time and Space Complexity: O(N)

        self.decreasing = {}
        self.increasing = {}

        return self.longestPathPassing(root)

    def longestPathPassing(self, node: TreeNode) -> int:
        ret = max(
            self.longestPathFrom(node, True)[0] + self.longestPathFrom(node, False)[1] - 1,
            self.longestPathFrom(node, False)[0] + self.longestPathFrom(node, True)[1] - 1
        )


        if node.left:
            ret = max(ret, self.longestPathPassing(node.left))

        if node.right:
            ret = max(ret, self.longestPathPassing(node.right))

        return ret

    def longestPathFrom(self, node: TreeNode, increasing: bool) -> Tuple[int, int, int]:
        if increasing:
            memoize_dict = self.increasing
        else:
            memoize_dict = self.decreasing

        if node in memoize_dict:
            return memoize_dict[node]

        left, right, longest = 1, 1, 1
        if node.left and self.same_direction(node, node.left, increasing):
            left = self.longestPathFrom(node.left, increasing)[-1] + 1

        if node.right and self.same_direction(node, node.right, increasing):
            right = self.longestPathFrom(node.right, increasing)[-1] + 1

        longest = max(left, right)
        memoize_dict[node] = left, right, longest
        return left, right, longest

    def same_direction(self, node1: TreeNode, node2: TreeNode, increasing: bool) -> bool:
        return (increasing and (node1.val + 1 == node2.val)) or (not increasing and (node1.val == node2.val + 1))
