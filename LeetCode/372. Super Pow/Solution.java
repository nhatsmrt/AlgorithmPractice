class Solution {
    private int[][] dp;
    public int superPow(int a, int[] b) {
        if (a > 1337)
            return superPow(a % 1337, b);

        dp = new int[10][b.length];
        dp[0][0] = 1;
        dp[1][0] = a;

        int ret = 1;
        for (int i = 0; i < b.length; i++) {
            ret *= superPow(a, b[b.length - 1 - i], i);
            ret %= 1337;
        }
        return ret;
    }

    private int superPow(int a, int digit, int tens) {
        if (dp[digit][tens] != 0)
            return dp[digit][tens];
        else if (digit > 1) {
            int ret = 1;
            int pow = 1;

            while (pow <= digit) {
                if (dp[pow][tens] == 0) {
                    if (pow == 1)
                        superPow(a, 1, tens);
                    else
                        dp[pow][tens] = (dp[pow / 2][tens] * dp[pow / 2][tens]) % 1337;
                }
                if ((digit & pow) > 0) {
                    ret *= dp[pow][tens];
                    ret %= 1337;
                }
                pow *= 2;
            }
            dp[digit][tens] = ret;
            return dp[digit][tens];
        }
        else {
            int tmp = superPow(a, digit, tens - 1);
            int tmpSq = (tmp * tmp) % 1337;
            int tmpPow8 = (tmpSq * tmpSq) % 1337;
            tmpPow8 = (tmpPow8 * tmpPow8) % 1337;
            dp[digit][tens] = (tmpSq * tmpPow8) % 1337;
            return dp[digit][tens];
        }
    }
}
