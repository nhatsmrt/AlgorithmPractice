class Solution2 {
    private int[][] dp;
    private int[][] moves;

    public int knightDialer(int N) {
        dp = new int[N][10];
        for (int[] subarr : dp)
            Arrays.fill(subarr, -1);

        moves = new int[][] {
            {4, 6}, {6, 8}, {7, 9}, {4, 8}, {0, 3, 9}, {},
            {0, 1, 7}, {2, 6}, {1 , 3}, {4, 2}, {4, 6}
        };
        int ret = 0;
        for (int i = 0; i < 10; i++) {
            ret += knightDialer(N - 1, i);
            ret %= 1000000007;
        }
        return ret;
    }

    private int knightDialer(int N, int pos) {
        if (N == 0)
            return 1;

        if (dp[N][pos] != -1)
            return dp[N][pos];

        int ret = 0;
        if (pos != 5) {
            ret = knightDialer(N - 1, moves[pos][0]);
            for (int i = 1; i < moves[pos].length; i++) {
                ret += knightDialer(N - 1, moves[pos][i]);
                ret %= 1000000007;
            }
        }

        dp[N][pos] = ret;
        return ret;
    }
}
