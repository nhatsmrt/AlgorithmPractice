# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # Time and Space Complexity: O(N)

        self.get_height(root)
        return self.dfs(root)

    def get_height(self, node: TreeNode) -> int:
        if node is None:
            return 0

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node.height

    def dfs(self, node: TreeNode) -> TreeNode:
        if node.left is None and node.right is None:
            return node
        elif node.left is None:
            return self.dfs(node.right)
        elif node.right is None:
            return self.dfs(node.left)
        elif node.left.height > node.right.height:
            return self.dfs(node.left)
        elif node.right.height > node.left.height:
            return self.dfs(node.right)
        else:
            return node
        
