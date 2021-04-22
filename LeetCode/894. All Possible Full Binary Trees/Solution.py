# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:

        cache = {}

        def generate(n: int):
            if n in cache:
                return cache[n]

            if n % 2 == 0:
                return []

            if n == 1:
                return [TreeNode()]

            ret = []

            for i in range(1, n, 2):
                lefts = generate(i)
                rights = generate(n - i - 1)

                for left in lefts:
                    for right in rights:
                        ret.append(TreeNode(0, left, right))

            cache[n] = ret
            return ret

        return generate(n)
