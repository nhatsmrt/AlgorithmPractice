class Solution {
    private int[][] dp;
    public int minScoreTriangulation(int[] A) {
        dp = new int[A.length][A.length];
        for (int i = 0; i < dp.length; i++)
            Arrays.fill(dp[i], -1);

        return minScore(A, 0, A.length - 1);
    }

    private int minScore(int[] A, int start, int end) {
        // dp[i][j] = min_{i < k < j}(dp[i][k] + dp[k][j] + cost(i,j,k))
        if (dp[start][end] != -1)
            return dp[start][end];

        int ret = -1;
        if (end - start + 1 == 3)
            ret = A[start] * A[start + 1] * A[end];
        else {
            for (int i = start + 1; i <= end - 1; i++) {
                int candidate = A[start] * A[end] * A[i];
                if (i - start + 1 >= 3)
                    candidate += minScore(A, start, i);
                if (end - i + 1 >= 3)
                    candidate += minScore(A, i, end);

                if (ret == -1 || ret > candidate)
                    ret = candidate;
            }
        }

        dp[start][end] = ret;
        return ret;
    }
}
