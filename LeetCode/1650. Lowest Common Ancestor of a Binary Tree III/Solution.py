"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
def find(node):
    ret = [node]

    while node.parent:
        node = node.parent
        ret.append(node)

    return ret[::-1]

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path, q_path = find(p), find(q)

        i = 0
        j = 0

        while i + 1 < len(p_path) and j + 1 < len(q_path) and p_path[i + 1] == q_path[j + 1]:
            i += 1
            j += 1

        return p_path[i]
