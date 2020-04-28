# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        # Time and Space Complexity: O(N)

        self.subtree_sum = {}
        self.compute_subtree_sum(root)
        return self.tree_walk(root)

    def tree_walk(self, node: TreeNode) -> bool:
        if node.left is not None:
            if self.subtree_sum[node.left] * 2 == self.subtree_sum[node] or self.reroot(node, node.left):
                return True

        if node.right is not None:
            if self.subtree_sum[node.right] * 2 == self.subtree_sum[node] or self.reroot(node, node.right):
                return True

        return False

    def reroot(self, node: TreeNode, child: TreeNode) -> bool:
            self.subtree_sum[node] -= self.subtree_sum[child]
            self.subtree_sum[child] += self.subtree_sum[node]

            ret = self.tree_walk(child)

            self.subtree_sum[child] -= self.subtree_sum[node]
            self.subtree_sum[node] += self.subtree_sum[child]

            return ret


    def compute_subtree_sum(self, node: TreeNode) -> int:
        ret = node.val

        if node.left is not None:
            ret += self.compute_subtree_sum(node.left)

        if node.right is not None:
            ret += self.compute_subtree_sum(node.right)

        self.subtree_sum[node] = ret
        return ret
