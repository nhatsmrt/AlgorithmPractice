class Solution:
    _MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def closedIsland(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(MN)

        ret = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    ret += int(self.floodfill(grid, i, j))

        return ret

    def floodfill(self, grid: List[List[int]], i: int, j: int):
        grid[i][j] = 2

        ret = i > 0 and i < len(grid) - 1 and j > 0 and j < len(grid[0]) - 1

        for move in self._MOVES:
            new_i, new_j = i + move[0], j + move[1]

            if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0]) and not grid[new_i][new_j]:
                ret = self.floodfill(grid, new_i, new_j) and ret

        return ret
