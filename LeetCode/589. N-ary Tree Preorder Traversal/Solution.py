"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        ret = []
        self.dfs(root, ret)

        return ret

    def dfs(self, node: 'Node', ret: List[int]):
        ret.append(node.val)

        for child in node.children:
            self.dfs(child, ret)
