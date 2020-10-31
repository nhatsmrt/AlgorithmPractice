# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        self.inorder(root, nodes)

        first, second = None, None
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                second = nodes[i + 1]

                if not first:
                    first = nodes[i]

        first.val, second.val = second.val, first.val

    def inorder(self, node, nodes):
        if node.left:
            self.inorder(node.left, nodes)

        nodes.append(node)

        if node.right:
            self.inorder(node.right, nodes)
