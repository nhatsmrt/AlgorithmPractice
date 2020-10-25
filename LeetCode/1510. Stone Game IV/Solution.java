class Solution {
    private int[] dp;

    public boolean winnerSquareGame(int n) {
        // Time Complexity: O(N sqrt(N))
        // Space Complexity: O(N)

        dp = new int[n + 1];
        Arrays.fill(dp, -1);

        return solve(n) == 1;
    }

    private int solve(int n) {
        if (dp[n] != -1) {
            return dp[n];
        }

        int sqrt = (int) Math.sqrt(n);
        int ret = 0;

        if (sqrt * sqrt == n) {
            ret = 1;
        }
        else {
            for (int i = sqrt; i > 0; i--) {
                if (solve(n - i * i) == 0) {
                    ret = 1;
                    break;
                }
            }
        }

        dp[n] = ret;
        return ret;
    }
}
