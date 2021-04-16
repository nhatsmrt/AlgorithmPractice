class Solution {
    private int[][][] dp;
    private final int MOD = 1000000007;

    public int checkRecord(int n) {
        // Time and Space Complexity: O(N)

        // dp[i][a][l]
        // where i is the number of remaining days
        // a is the total number of absent day so far (a < 2)
        // l is number of consecutive late day up to now (l < 3)
        // answer is dp[n][0][0]


        dp = new int[n + 1][2][3];

        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 3; k++)
                    dp[i][j][k] = -1;
            }
        }

        return count(n, 0, 0);
    }

    private int count(int days, int absent, int consecLate) {
        if (days == 0)
            return 1;

        if (dp[days][absent][consecLate] >= 0)
            return dp[days][absent][consecLate];

        int ret = count(days - 1, absent, 0); // on time
        if (absent < 1) {
            ret += count(days - 1, absent + 1, 0); // absent
            ret %= MOD;
        }

        if (consecLate < 2) {
            ret += count(days - 1, absent, consecLate + 1); // late
            ret %= MOD;
        }

        dp[days][absent][consecLate] = ret;
        return ret;
    }
}
