class Solution {
    // O(KN) solution
    private int[] dp;

    public int superEggDrop(int K, int N) {
        dp = new int[N + 1];
        for (int i = 0; i <= N; i++)
            dp[i] = i;

        for (int k = 2; k <= K; k++) {
            int[] dpNext = new int[N + 1];
            int f = 1;
            for (int n = 1; n <= N; n++) {
                while (f < n && Math.max(dp[f - 1], dpNext[n - f]) > Math.max(dp[f], dpNext[n - f - 1]))
                    f += 1;
                dpNext[n] = 1 + Math.max(dp[f - 1], dpNext[n - f]);
            }
            dp = dpNext;
        }

        return dp[N];
    }

}
