class Solution {
    private int[][][] dp;

    public int cherryPickup(int[][] grid) {
        // Observation 1: Instead of walking from (0, 0) to (N-1, N-1)
        // we can think of the problem as two ppl walking from (0, 0) to (N-1, N-1)
        // using only down and right move

        // Observation 2: After l steps, if the position the person ends up is (r, c)
        // then r + c = l

        // Observation 3: If these two ppl are at layer l (i.e r1 + c1 = l, r2 + c2 = l)
        // one person cannot go to a cell that the other has visited in the first t moves
        // since they can only move right and down
        // This allows us to create a state space of O(N^4) for the DP solution.

        // Observation 4: Since we know that r_1 + c_1 = r_2 + c_2 = l, we only need to keep
        // track of 3 out of these 4 numbers, reducing the state space to O(N^3)

        // Time Complexity: O(N^3), Space Complexity: O(N^3)

        int N = grid.length;
        dp = new int[N][N][N];
        for (int[][] arr1 : dp) {
            for (int[] arr2 : arr1)
                Arrays.fill(arr2, -1);
        }

        dp[N - 1][N - 1][N - 1] = grid[N - 1][N - 1];

        int ret = cherryPickup(grid, 0, 0, 0);
        return 0 > ret ? 0 : ret;
    }

    private int cherryPickup(int[][] grid, int r1, int c1, int r2) {
        if (dp[r1][c1][r2] != -1)
            return dp[r1][c1][r2];

        int c2 = r1 + c1 - r2;
        int ret = -2;

        if (isLegal(grid, r1 + 1, c1) && isLegal(grid, r2 + 1, c2))
            ret = attempt(grid, ret, r1 + 1, c1, r2 + 1);

        if (isLegal(grid, r1, c1 + 1) && isLegal(grid, r2 + 1, c2))
            ret = attempt(grid, ret, r1, c1 + 1, r2 + 1);

        if (isLegal(grid, r1 + 1, c1) && isLegal(grid, r2, c2 + 1))
            ret = attempt(grid, ret, r1 + 1, c1, r2);

        if (isLegal(grid, r1, c1 + 1) && isLegal(grid, r2, c2 + 1))
            ret = attempt(grid, ret, r1, c1 + 1, r2);

        if (ret != -2) {
            ret += grid[r1][c1];
            if (r1 != r2)
                ret += grid[r2][c2];
        }

        dp[r1][c1][r2] = ret;
        return ret;
    }

    private boolean isLegal(int[][] grid, int i, int j) {
        return i < grid.length && j < grid.length && grid[i][j] != -1;
    }

    private int attempt(int[][] grid, int ret, int newR1, int newC1, int newR2) {
        int candidate = cherryPickup(grid, newR1, newC1, newR2);
        return ret < candidate ? candidate : ret;
    }
}
