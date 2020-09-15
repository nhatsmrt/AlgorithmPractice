"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        it = node
        go_up_from_left = False
        go_up_from_right = False
        go_right = False

        while not go_right:
            if not go_up_from_right and it.right:
                it = it.right
                go_right = True
            elif it.parent is None:
                return None
            elif it == it.parent.left:
                return it.parent
            else:
                go_up_from_left = False
                go_up_from_right = True

                it = it.parent

        while it.left:
            it = it.left

        return it
