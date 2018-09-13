class Solution {
    int[][] paths = new int[101][101];
    public int uniquePathsTo(int m, int n, int[][] obstacleGrid) {
        if (obstacleGrid[m][n] == 1) {
            paths[m][n] = 0;
            return 0;
        }

        if (m == 0 && n == 0) {
            paths[0][0] = 1 - obstacleGrid[0][0];
            return paths[0][0];
        }

        if (m == 0) {
            paths[0][n] = uniquePathsTo(0, n - 1, obstacleGrid);
            return paths[0][n];
        }

        if (n == 0) {
            paths[m][0] = uniquePathsTo(m - 1, 0, obstacleGrid);
            return paths[m][0];
        }

        if (paths[m][n] != -1)
            return paths[m][n];

        paths[m][n] = uniquePathsTo(m - 1, n, obstacleGrid) + uniquePathsTo(m, n - 1, obstacleGrid);
        return paths[m][n];
    }


    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        for (int[] array : paths)
            Arrays.fill(array, -1);

        int w = obstacleGrid.length;
        int h = obstacleGrid[0].length;

        return uniquePathsTo(w - 1, h - 1, obstacleGrid);
    }
}
