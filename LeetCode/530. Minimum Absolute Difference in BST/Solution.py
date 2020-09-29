# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        vals = []
        self.inorder(root, vals)

        ret = 1000000000
        for i in range(len(vals) - 1):
            ret = min(ret, vals[i + 1] - vals[i])

        return ret

    def inorder(self, node: TreeNode, ret: List[int]):
        if node:
            self.inorder(node.left, ret)
            ret.append(node.val)
            self.inorder(node.right, ret)
