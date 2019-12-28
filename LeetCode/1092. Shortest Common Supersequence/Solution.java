class Solution {
    private int[][] dp;
    private int[][] next;

    public String shortestCommonSupersequence(String str1, String str2) {
        dp = new int[str1.length()][str2.length()];
        next = new int[str1.length()][str2.length()];

        shortestCS(str1, str2, 0, 0);
        StringBuilder ret = new StringBuilder();
        buildSCS(ret, str1, str2, 0, 0);
        return ret.toString();
    }

    private int shortestCS(String s1, String s2, int i, int j) {
        if (i == s1.length())
            return s2.length() - j;

        if (j == s2.length())
            return s1.length() - i;

        if (dp[i][j] != 0)
            return dp[i][j];

        int candidate1 = 1 + shortestCS(s1, s2, i + 1, j);
        int candidate2 = 1 + shortestCS(s1, s2, i, j + 1);
        int ret;

        if (candidate1 < candidate2) {
            ret = candidate1;
            next[i][j] = 0;
        }
        else {
            ret = candidate2;
            next[i][j] = 1;
        }

        if (s1.charAt(i) == s2.charAt(j)) {
            int candidate3 = 1 + shortestCS(s1, s2, i + 1, j + 1);
            if (candidate3 < ret) {
                ret = candidate3;
                next[i][j] = 2;
            }
        }

        dp[i][j] = ret;
        return ret;
    }

    private void buildSCS(StringBuilder str, String s1, String s2, int i, int j) {
        if (i == s1.length())
            str.append(s2.substring(j));
        else if (j == s2.length())
            str.append(s1.substring(i));
        else {
            if (next[i][j] == 0) {
                str.append(s1.charAt(i));
                buildSCS(str, s1, s2, i + 1, j);
            }
            else if (next[i][j] == 1) {
                str.append(s2.charAt(j));
                buildSCS(str, s1, s2, i, j + 1);

            }
            else {
                str.append(s1.charAt(i));
                buildSCS(str, s1, s2, i + 1, j + 1);
            }
        }
    }
}
