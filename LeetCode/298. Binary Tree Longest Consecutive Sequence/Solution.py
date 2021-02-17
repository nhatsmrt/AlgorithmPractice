# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.builPath(root, 0)

    def builPath(self, node: TreeNode, length_so_far: int) -> int:
        ret = length_so_far + 1

        if node.left:
            if node.left.val == node.val + 1:
                ret = max(ret, self.builPath(node.left, length_so_far + 1))
            else:
                ret = max(ret, self.builPath(node.left, 0))

        if node.right:
            if node.right.val == node.val + 1:
                ret = max(ret, self.builPath(node.right, length_so_far + 1))
            else:
                ret = max(ret, self.builPath(node.right, 0))

        return ret
