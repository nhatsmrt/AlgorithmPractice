class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret = max(ret, self.floodFill(grid, i, j))

        return ret

    def floodFill(self, grid: List[List[int]], i: int, j: int) -> int:
        if grid[i][j] == 0 or grid[i][j] == 2:
            return 0

        grid[i][j] = 2
        ret = 1
        if i > 0:
            ret += self.floodFill(grid, i - 1, j)

        if i < len(grid) - 1:
            ret += self.floodFill(grid, i + 1, j)

        if j > 0:
            ret += self.floodFill(grid, i, j - 1)

        if j < len(grid[0]) - 1:
            ret += self.floodFill(grid, i, j + 1)

        return ret
        
