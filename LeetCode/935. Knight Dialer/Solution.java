class Solution {
    private int[][] dp;

    public int knightDialer(int N) {
        dp = new int[N][10];
        for (int[] subarr : dp)
            Arrays.fill(subarr, -1);
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
        switch (pos) {
            case 1: ret = knightDialer(N - 1, 6) + knightDialer(N - 1, 8);
                break;
            case 2: ret = knightDialer(N - 1, 7) + knightDialer(N - 1, 9);
                break;
            case 3: ret = knightDialer(N - 1, 4) + knightDialer(N - 1, 8);
                break;
            case 4:
                ret = (knightDialer(N - 1, 3) + knightDialer(N - 1, 9)) % 1000000007 +
                    knightDialer(N - 1, 0);
                break;
            case 5: break;
            case 6:
                ret = (knightDialer(N - 1, 1) + knightDialer(N - 1, 7)) % 1000000007 +
                    knightDialer(N - 1, 0);
                break;
            case 7: ret = knightDialer(N - 1, 2) + knightDialer(N - 1, 6);
                break;
            case 8: ret = knightDialer(N - 1, 1) + knightDialer(N - 1, 3);
                break;
            case 9: ret = knightDialer(N - 1, 4) + knightDialer(N - 1, 2);
                break;
            case 0: ret = knightDialer(N - 1, 4) + knightDialer(N - 1, 6);
                break;

        }
        ret %= 1000000007;

        dp[N][pos] = ret;
        return ret;
    }
}
