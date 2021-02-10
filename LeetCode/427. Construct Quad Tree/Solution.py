"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.constructSubTree(grid, 0, len(grid) - 1, 0, len(grid[0]) - 1)

    def constructSubTree(self, grid: List[List[int]], xmin: int, xmax: int, ymin: int, ymax: int) -> 'Node':
        if xmin == xmax:
            # also implying ymin == ymax
            return Node(grid[xmin][ymin] == 1, True, None, None, None, None)
        else:
            xmid = (xmin + xmax) // 2
            ymid = (ymin + ymax) // 2

            topLeft = self.constructSubTree(grid, xmin, xmid, ymin, ymid)
            topRight = self.constructSubTree(grid, xmin, xmid, ymid + 1, ymax)
            bottomLeft = self.constructSubTree(grid, xmid + 1, xmax, ymin, ymid)
            bottomRight = self.constructSubTree(grid, xmid + 1, xmax, ymid + 1, ymax)

            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val and topRight.val == bottomLeft.val and bottomLeft.val == bottomRight.val:
                # same value in the entire subgrid
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
