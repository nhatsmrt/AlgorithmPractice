# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        return self.rotate(root, None, None)

    def rotate(self, node: TreeNode, new_left: TreeNode, new_right: TreeNode):
        old_left, old_right = node.left, node.right
        node.left, node.right = new_left, new_right

        if old_left is None:
            return node # new root

        return self.rotate(old_left, old_right, node)
