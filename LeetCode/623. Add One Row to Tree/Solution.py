# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # Time Complexity: O(N)

        if d == 1:
            return TreeNode(v, root)

        return self.insert(root, v, d - 2)

    def insert(self, node: int, val: int, remain_depth: int):
        if remain_depth:
            if node.left:
                node.left = self.insert(node.left, val, remain_depth - 1)

            if node.right:
                node.right = self.insert(node.right, val, remain_depth - 1)

        else:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)


        return node
