class Solution {
    public int uniquePathsIII(int[][] grid) {
        int[][] status = new int[grid.length][grid[0].length];

        int numRemaining = grid.length * grid[0].length;
        int start1 = 0;
        int start2 = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == -1) {
                    status[i][j] = -1;
                    numRemaining -= 1;
                }
                else if (grid[i][j] == 1) {
                    start1 = i;
                    start2 = j;
                    numRemaining -= 1;
                    status[i][j] = 1;
                }
                else
                    status[i][j] = 0;
            }
        }

        return countUniquePath(grid, status, start1, start2, numRemaining);
    }


    private int countUniquePath(
        int[][] grid, int[][] status, int i, int j, int numRemaining
    ) {
        int ret = 0;

        if (grid[i][j] == 2) {
            if (numRemaining == 0)
                return 1;
            else
                return 0;
        }


        if (i > 0 && status[i - 1][j] == 0) {
            status[i - 1][j] = 1;
            ret += countUniquePath(grid, status, i - 1, j, numRemaining - 1);
            status[i - 1][j] = 0;
        }

        if (i < grid.length - 1 && status[i + 1][j] == 0) {
            status[i + 1][j] = 1;
            ret += countUniquePath(grid, status, i + 1, j, numRemaining - 1);
            status[i + 1][j] = 0;
        }

        if (j > 0 && status[i][j - 1] == 0) {
            status[i][j - 1] = 1;
            ret += countUniquePath(grid, status, i, j - 1, numRemaining - 1);
            status[i][j - 1] = 0;
        }

        if (j < grid[0].length - 1 && status[i][j + 1] == 0) {
            status[i][j + 1] = 1;
            ret += countUniquePath(grid, status, i, j + 1, numRemaining - 1);
            status[i][j + 1] = 0;
        }

        return ret;
    }

}
