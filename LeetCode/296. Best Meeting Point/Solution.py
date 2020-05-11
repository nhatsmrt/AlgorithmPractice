class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # Time and Space Complexity: O(MN)

        xs = []
        ys = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    xs.append(i)

        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    ys.append(j)

        median = xs[len(xs) // 2], ys[len(ys) // 2]

        ret = 0
        for i in range(len(xs)):
            ret += abs(median[0] - xs[i]) + abs(median[1] - ys[i])

        return ret


        
