class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # 2D L1 distance transform
        # Time and Space Complexity: O(MN)

        dists = [
            [0 if grid[i][j] == 1 else 1000000000 for j in range(len(grid[0]))]
            for i in range(len(grid))
        ]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0:
                    dists[i][j] = min(dists[i][j], dists[i - 1][j] + 1)

                if j > 0:
                    dists[i][j] = min(dists[i][j], dists[i][j - 1] + 1)

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i + 1 < len(grid):
                    dists[i][j] = min(dists[i][j], dists[i + 1][j] + 1)

                if j + 1 < len(grid[0]):
                    dists[i][j] = min(dists[i][j], dists[i][j + 1] + 1)

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret = max(ret, dists[i][j])

        if ret == 1000000000 or ret == 0:
            return -1

        return ret

        
