class Solution {
    private int[][] dp;

    public int kInversePairs(int n, int k) {
        dp = new int[n][k + 1];
        for (int[] arr : dp)
            Arrays.fill(arr, -1);
        return kInversePairsDP(n, k);
    }

    private int kInversePairsDP(int n, int k) {
        if (k == 0)
            return 1;
        if (n == 1) {
            if (k == 0)
                return 1;
            return 0;
        }

        if (dp[n - 1][k] != -1)
            return dp[n - 1][k];

        int ret = (kInversePairsDP(n, k - 1) + kInversePairsDP(n - 1, k)) % 1000000007;

        int lowerBound = k - Math.min(n - 1, k);
        int oldLowerBound = k - 1 - Math.min(n - 1, k - 1);

        for (int i = oldLowerBound; i < lowerBound; i++) {
            ret -= kInversePairsDP(n - 1, i);
            ret += 1000000007;
            ret %= 1000000007;
        }


        dp[n - 1][k] = ret;
        return ret;
    }
}
