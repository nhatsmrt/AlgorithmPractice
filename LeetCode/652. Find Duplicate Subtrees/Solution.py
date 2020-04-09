# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # O(n) time and space complexity
        self.merkle2node = {}
        self.merkle(root)

        ret = []
        for key in self.merkle2node:
            if len(self.merkle2node[key]) > 1:
                ret.append(self.merkle2node[key][0])

        return ret

    def merkle(self, node: TreeNode) -> str:
        if node is None:
            return "#"

        left = self.merkle(node.left)
        right = self.merkle(node.right)
        node.merkle = self.hash_fn(left + str(node.val) + right)

        if node.merkle not in self.merkle2node:
            self.merkle2node[node.merkle] = []
        self.merkle2node[node.merkle].append(node)

        return node.merkle

    def hash_fn(self, key: str) -> str:
        from hashlib import sha256
        S = sha256()
        S.update(key.encode("utf-8"))
        return S.hexdigest()
