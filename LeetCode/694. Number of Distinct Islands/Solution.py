import hashlib


class Solution:
    MOVES = [
        (0, 1), (1, 0), (-1, 0), (0, -1)
    ]

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(MN)
        # It takes linear time to go through each cell in the flood fill.
        # Each cell goes into the tree exactly once.
        # The tree's hash has constant size.
        # Space Complexity: O(MN) (each tree takes up constant size)

        islands = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islands.add(self.floodfill(i, j, grid))

        return len(islands)

    def floodfill(self, i: int, j: int, grid: List[List[int]]):
        m = hashlib.sha256()
        grid[i][j] = 2
        children = []

        for move_i, move_j in self.MOVES:
            new_i, new_j = i + move_i, j + move_j
            if self.is_valid(new_i, new_j, grid):
                children.append(b"(" + self.floodfill(new_i, new_j, grid) + b")")
            else:
                children.append(b"()")

        m.update(b"$")
        for child in children:
            m.update(child)
        return m.digest()


    def is_valid(self, i, j, grid):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1
