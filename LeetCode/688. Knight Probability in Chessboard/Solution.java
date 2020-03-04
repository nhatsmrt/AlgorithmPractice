class Solution {
    private int[][] moves = {{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}};
    private double[][][] dp;

    public double knightProbability(int N, int K, int r, int c) {
        // Time and Space Complexity: O(N^2 K)
        dp = new double[N][N][K];
        for (double[][] subarr : dp) {
            for (double[] subarr2 : subarr)
                Arrays.fill(subarr2, -1.0);
        }

        return probDP(N, K, r, c);
    }

    private double probDP(int N, int K, int r, int c) {
        if (r < 0 || r >= N || c < 0 || c >= N)
            return 0.0;
        if (K == 0)
            return 1.0;

        if (dp[r][c][K - 1] != -1.0)
            return dp[r][c][K - 1];

        double ret = 0.0;
        for (int[] move : moves) {
            ret += 0.125 * probDP(N, K - 1, r + move[0], c + move[1]);
        }

        dp[r][c][K - 1] = ret;
        return ret;
    }
}
