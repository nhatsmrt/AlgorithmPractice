# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            return self.find_leftmost(p.right)


        path = [root]
        self.find_path(root, p, path)

        for i in range(len(path) - 2, -1, -1):
            if path[i].left == path[i + 1]:
                return path[i]

        return None

    def find_leftmost(self, node):
        it = node

        while it.left:
            it = it.left

        return it

    def find_path(self, node, p, ret):
        if node:
            if node.val < p.val:
                ret.append(node.right)
                self.find_path(node.right, p, ret)
            elif node.val > p.val:
                ret.append(node.left)
                self.find_path(node.left, p, ret)
