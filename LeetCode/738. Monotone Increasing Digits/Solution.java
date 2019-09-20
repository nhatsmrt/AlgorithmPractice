class Solution {
    private int[][][] dp;
    public int monotoneIncreasingDigits(int N) {
        if (N < 10)
            return N;

        int scale = 1;
        int numDig = 1;
        while (scale * 10 <= N) {
            scale *= 10;
            numDig += 1;
        }

        int[] Ndigs = new int[numDig];
        for (int i = 0; i < Ndigs.length; i++) {
            Ndigs[i] = N / scale;
            N %= scale;
            scale /= 10;
        }

        dp = new int[10][numDig][2];
        for (int i = 0; i < 10; i++) {
            for (int d = 0; d < numDig; d++)
                dp[i][d][0] = dp[i][d][1] = -1;
        }

        return monotoneIncreasingDigits(Ndigs, 0, 0, 0);
    }

    private int monotoneIncreasingDigits(int[] Ndigs, int curMax, int pos, int safe) {
        if (pos >= Ndigs.length)
            return 0;

        if (dp[curMax][pos][safe] != -1)
            return dp[curMax][pos][safe];

        int ret = -1;
        if (safe == 1) {
            ret = 1;
            for (int i = pos; i < Ndigs.length; i++)
                ret *= 10;
            ret -= 1;
        }
        else {
            if (curMax <= Ndigs[pos]) {
                for (int i = curMax; i <= Ndigs[pos]; i++) {
                    int newSafe = i == Ndigs[pos] ? 0 : 1;
                    int candidate = monotoneIncreasingDigits(Ndigs, i, pos + 1, newSafe);
                    if (candidate >= 0) {
                        int scale = 1;
                        while (scale <= candidate)
                            scale *= 10;
                        candidate += i * scale;
                        if (candidate > ret)
                            ret = candidate;
                    }
                    else
                        break;
                }
            }
        }

        dp[curMax][pos][safe] = ret;
        return ret;
    }
}
