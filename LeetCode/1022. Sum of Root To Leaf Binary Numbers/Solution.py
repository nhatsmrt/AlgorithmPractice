# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0

        acc = [0]
        self.sumPath(root, root.val, acc)
        return acc[0]

    def sumPath(self, node: TreeNode, partial: int, acc: List[int]) -> int:
        if not (node.left or node.right):
            acc[0] += partial

        if node.left:
            self.sumPath(node.left, 2 * partial + node.left.val, acc)

        if node.right:
            self.sumPath(node.right, 2 * partial + node.right.val, acc)
