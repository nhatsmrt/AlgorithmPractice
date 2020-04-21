# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Dict

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Time and Space Complexity: O(N)

        merkle2node = {}
        self.merkle(cloned, merkle2node)

        return merkle2node[self.merkle(target, None)]

    def merkle(self, node: TreeNode, merkle2node: Dict[str, TreeNode]) -> str:
        if node is None:
            return "#"

        ret = self.hash_fn(self.merkle(node.left, merkle2node) + str(node.val) + self.merkle(node.right, merkle2node))

        if merkle2node is not None:
            merkle2node[ret] = node

        return ret

    def hash_fn(self, key: str) -> str:
        from hashlib import sha256
        S = sha256()
        S.update(key.encode('utf-8'))
        return S.hexdigest()
