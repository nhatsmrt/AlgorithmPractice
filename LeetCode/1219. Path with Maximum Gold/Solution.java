class Solution {
    public int getMaximumGold(int[][] grid) {
        int[][] status = new int[grid.length][grid[0].length];
        int ret = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] > 0) {
                    int candidate = grid[i][j] + maxFrom(grid, status, i, j);
                    if (candidate > ret)
                        ret = candidate;
                }
            }
        }

        return ret;
    }

    private int maxFrom(int[][] grid, int[][] status, int i, int j) {
        status[i][j] = 1;
        int ret = 0;

        if (i > 0 && status[i - 1][j] == 0 && grid[i - 1][j] > 0) {
            int candidate = grid[i - 1][j] + maxFrom(grid, status, i - 1, j);
            if (ret < candidate)
                ret = candidate;
        }

        if (i < grid.length - 1 && status[i + 1][j] == 0 && grid[i + 1][j] > 0) {
            int candidate = grid[i + 1][j] + maxFrom(grid, status, i + 1, j);
            if (ret < candidate)
                ret = candidate;
        }

        if (j > 0 && status[i][j - 1] == 0 && grid[i][j - 1] > 0) {
            int candidate = grid[i][j - 1] + maxFrom(grid, status, i, j - 1);
            if (ret < candidate)
                ret = candidate;
        }

        if (j < grid[0].length - 1 && status[i][j + 1] == 0 && grid[i][j + 1] > 0) {
            int candidate = grid[i][j + 1] + maxFrom(grid, status, i, j + 1);
            if (ret < candidate)
                ret = candidate;
        }

        status[i][j] = 0;
        return ret;
    }
}
