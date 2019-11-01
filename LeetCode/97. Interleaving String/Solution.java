class Solution {
    private int[][] dp;

    public boolean isInterleave(String s1, String s2, String s3) {
        if (s3.length() != s1.length() + s2.length())
            return false;

        dp = new int[s1.length()][s2.length()];
        for (int i = 0; i < s1.length(); i++)
            Arrays.fill(dp[i], -1);

        return isInterleave(s1, s2, s3, 0, 0) == 0;
    }

    private int isInterleave(String s1, String s2, String s3, int i, int j) {
        if (i == s1.length() && j == s2.length())
            return 0;

        if (i == s1.length()) {
            if (s3.charAt(i + j) == s2.charAt(j))
                return isInterleave(s1, s2, s3, i, j + 1);
            else
                return 1;
        }

        if (j == s2.length()) {
            if (s3.charAt(i + j) == s1.charAt(i))
                return isInterleave(s1, s2, s3, i + 1, j);
            else
                return 1;
        }

        if (dp[i][j] != -1)
            return dp[i][j];

        int ret = 1;
        if (s3.charAt(i + j) == s1.charAt(i) && isInterleave(s1, s2, s3, i + 1, j) == 0)
            ret = 0;
        else if (s3.charAt(i + j) == s2.charAt(j) && isInterleave(s1, s2, s3, i, j + 1) == 0)
            ret = 0;

        dp[i][j] = ret;
        return ret;
    }


}
