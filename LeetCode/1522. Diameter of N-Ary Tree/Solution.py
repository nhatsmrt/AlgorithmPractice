"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        # Time and Space Complexity: O(N)
        self.in_diam = {}
        self.best_children = {}
        self.par = {}

        self.in_dp(root)
        return self.compute_diam(root)

    def compute_diam(self, node: 'Node') -> int:
        # diam through node:
        ret = self.in_diam[node]

        if node in self.par:
            best_sibling, second_sibbling = self.best_children[self.par[node]]

            if best_sibling and best_sibling[0] != node:
                ret += 2 + best_sibling[1]
            elif second_sibbling:
                ret += 2 + second_sibbling[1]

        for child in node.children:
            ret = max(ret, self.compute_diam(child))

        return ret

    def in_dp(self, node: 'Node') -> int:
        if not node:
            return 0

        if node in self.in_diam:
            return self.in_diam[node]

        children_in_diam = [(child, self.in_dp(child)) for child in node.children]
        ret = 0
        best, second = None, None

        for child, child_in in children_in_diam:
            self.par[child] = node

            if best is None or best[1] < child_in:
                second = best
                best = child, child_in
            elif second is None or second[1] < child_in:
                second = child, child_in

        if best:
            ret += 1 + best[1]

        self.in_diam[node] = ret
        self.best_children[node] = best, second
        return ret
