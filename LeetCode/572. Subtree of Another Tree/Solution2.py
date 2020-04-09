# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Based on https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.merkle(s)
        self.merkle(t)

        return self.subtree_check(s, t)

    def merkle(self, node: TreeNode) -> str:
        if node is None:
            return "#"

        left = self.merkle(node.left)
        right = self.merkle(node.right)
        merkle = self.hash_fn(left + str(node.val) + right)

        node.merkle = merkle
        return merkle

    def hash_fn(self, key: str) -> int:
        from hashlib import sha256
        S = sha256()
        S.update(key.encode('utf-8'))
        return S.hexdigest()

    def subtree_check(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 is None:
            return False

        return node1.merkle == node2.merkle or self.subtree_check(node1.left, node2) or self.subtree_check(node1.right, node2)

        
