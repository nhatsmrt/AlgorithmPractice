class Solution {
    private int[][] dp;

    public int findLength(int[] A, int[] B) {
        dp = new int[A.length][B.length];

        for (int[] subarr : dp)
            Arrays.fill(subarr, -1);

        int ret = 0;
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A.length; j++) {
                ret = Math.max(ret, lcp(A, B, i, j));
            }
        }

        return ret;
    }

    private int lcp(int[] A, int[] B, int i, int j) {
        if (i == A.length || j == B.length)
            return 0;

        if (dp[i][j] != -1)
            return dp[i][j];

        int ret = 0;
        if (A[i] == B[j])
            ret = 1 + lcp(A, B, i + 1, j + 1);

        dp[i][j] = ret;
        return ret;
    }
}
