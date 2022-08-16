# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # Time and Space Complexity: O(N)

        if not root:
            return 0

        self.in_map = {}
        self.out = {}

        self.computeIn(root)
        self.computeOut(root, None)

        ret = 0
        for node in self.in_map:
            ret = max(ret, self.in_map[node] + self.out[node] - 2)

            if node.left and node.right and node.left.val == node.val and node.right.val == node.val:
                ret = max(ret, self.in_map[node.left] + self.in_map[node.right])

        return ret

    def computeOut(self, node, par):
        if not par or node.val != par.val:
            ret = 1
        else:
            ret = 1 + self.out[par]

            if node == par.left and par.right and par.right.val == par.val:
                ret = max(ret, self.in_map[par.right] + 2)
            elif node == par.right and par.left and par.left.val == par.val:
                ret = max(ret, self.in_map[par.left] + 2)

        self.out[node] = ret

        if node.left:
            self.computeOut(node.left, node)

        if node.right:
            self.computeOut(node.right, node)

    def computeIn(self, node):
        if not node:
            return 0

        left_in, right_in = self.computeIn(node.left), self.computeIn(node.right)
        ret = 1

        if node.left and node.val == node.left.val:
            ret = left_in + 1

        if node.right and node.val == node.right.val:
            ret = max(ret, right_in + 1)

        self.in_map[node] = ret
        return ret
