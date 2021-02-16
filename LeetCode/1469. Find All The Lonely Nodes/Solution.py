# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        # Time and Space Complexity: O(N)

        ret = []
        self.dfs(root, ret)
        return ret

    def dfs(self, node: TreeNode, ret: List[TreeNode]):
        if node.left or node.right:
            if not node.left:
                ret.append(node.right.val)

            if not node.right:
                ret.append(node.left.val)

            if node.left:
                self.dfs(node.left, ret)

            if node.right:
                self.dfs(node.right, ret)
