class Solution {
    int[][] pathSum;
    public int minPathSumDP(int[][] grid, int i, int j) {
        if (pathSum[i][j] != -1)
            return pathSum[i][j];

        int fromTop = minPathSumDP(grid, i - 1, j);
        int fromLeft = minPathSumDP(grid, i, j - 1);

        int ret = fromTop < fromLeft ? fromTop + grid[i][j] : fromLeft + grid[i][j];
        pathSum[i][j] = ret;

        return ret;
    }
    public int minPathSum(int[][] grid) {
        int numRow = grid.length;
        int numCol = grid[0].length;

        pathSum = new int[numRow][numCol];
        for (int[] row : pathSum)
            Arrays.fill(row, -1);

        for (int i = 0; i < numRow; i++) {
            if (i == 0)
                pathSum[i][0] = grid[0][0];
            else
                pathSum[i][0] = grid[i][0] + pathSum[i - 1][0];
        }

        for (int j = 0; j < numCol; j++) {
            if (j == 0)
                pathSum[0][j] = grid[0][0];
            else
                pathSum[0][j] = grid[0][j] + pathSum[0][j - 1];
        }

        return minPathSumDP(grid, numRow - 1, numCol - 1);
    }
}
