class Solution {
    private int dp[];

    public int numDecodings(String s) {
        dp = new int[s.length()];
        Arrays.fill(dp, -1);

        return numDecodings(s, 0);
    }

    private int numDecodings(String s, int i) {
        if (i == s.length())
            return 1;

        if (s.charAt(i) == '0')
            return 0;

        if (dp[i] != -1)
            return dp[i];

        int ret = 0;
        if (i < s.length() - 1 && s.charAt(i + 1) == '0') {
            if (s.charAt(i) == '*')
                ret = (2 * numDecodings(s, i + 2)) % 1000000007;
            else if (s.charAt(i) > '2')
                ret = 0;
            else
                ret = numDecodings(s, i + 2) % 1000000007;
        }
        else if (s.charAt(i) == '*') {
            ret = numDecodings(s, i + 1);
            ret += (ret * 2) % 1000000007;
            ret %= 1000000007;
            ret += (ret * 2) % 1000000007;
            ret %= 1000000007;

            if (i < s.length() - 1) {
                if (s.charAt(i + 1) == '*') {
                    int inc = numDecodings(s, i + 2);
                    inc += (2 * inc) % 1000000007;
                    inc %= 1000000007;

                    int twoInc = inc * 2;
                    twoInc %= 1000000007;
                    twoInc *= 2;
                    twoInc %= 1000000007;
                    inc += twoInc;
                    inc %= 1000000007;

                    ret += inc;
                    ret %= 1000000007;
                }
                else {
                    ret += numDecodings(s, i + 2); // * => 1
                    ret %= 1000000007;
                    if (s.charAt(i + 1) <= '6') {
                        ret += numDecodings(s, i + 2);
                        ret %= 1000000007;
                    }
                }
            }
        }
        else {
            ret = numDecodings(s, i + 1);
            if (i < s.length() - 1) {
                if (s.charAt(i) == '1') {
                    if (s.charAt(i + 1) == '*') {
                        int inc = numDecodings(s, i + 2);
                        inc += (2 * inc) % 1000000007;
                        inc %= 1000000007;
                        inc += (2 * inc) % 1000000007;
                        inc %= 1000000007;

                        ret += inc;
                    }
                    else
                        ret += numDecodings(s, i + 2);
                    ret %= 1000000007;
                }
                else if (s.charAt(i) == '2') {
                    if (s.charAt(i + 1) == '*') {
                        int inc = numDecodings(s, i + 2);
                        inc += (2 * inc) % 1000000007;
                        inc %= 1000000007;
                        inc *= 2;
                        inc %= 1000000007;

                        ret += inc;
                    }
                    else if (s.charAt(i + 1) <= '6')
                        ret += numDecodings(s, i + 2);
                    ret %= 1000000007;
                }
            }
        }

        dp[i] = ret;
        return ret;
    }
}
