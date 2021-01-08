"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        flag = 0

        for node in tree:
            flag = flag ^ node.val

            for child in node.children:
                flag = flag ^ child.val

        for node in tree:
            if node.val == flag:
                return node
