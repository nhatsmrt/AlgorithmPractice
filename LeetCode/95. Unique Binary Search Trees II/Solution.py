# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Time and Space Complexty: O(n Catalan(n))

        self.dp = {}
        return self.cachedGenerate(n, 1)

    def cachedGenerate(self, n: int, start: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [None]

        if (n, start) in self.dp:
            return self.dp[(n, start)]

        ret = []

        for i in range(0, n):

            lefts = self.cachedGenerate(i, start)
            rights = self.cachedGenerate(n - i - 1, start + i + 1)

            for left in lefts:
                for right in rights:
                    ret.append(TreeNode(start + i, left, right))

        self.dp[(n, start)] = ret
        return ret
        
