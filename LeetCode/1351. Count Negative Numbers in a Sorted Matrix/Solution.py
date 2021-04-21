class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(N + M)

        if grid[0][0] < 0:
            return len(grid) * len(grid[0])

        low = 0
        high = len(grid[0]) - 1
        col = 0
        while low < high:
            mid = high - (high - low) // 2

            if grid[0][mid] >= 0:
                low = mid
            else:
                high = mid - 1

        col = low
        numPos = col + 1
        for row in range(1, len(grid)):
            while col >= 0 and grid[row][col] < 0:
                col -= 1

            numPos += col + 1

        return len(grid) * len(grid[0]) - numPos
