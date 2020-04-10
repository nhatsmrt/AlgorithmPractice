class Solution {
    private int[][] dp;

    public int numDistinct(String s, String t) {
        // Time and space complexity: O(st)
        dp = new int[s.length()][t.length()];
        for (int[] subarr : dp)
            Arrays.fill(subarr, -1);

        return numDistinct(s, t, 0, 0);
    }

    private int numDistinct(String s, String t, int i, int j) {
        if (j == t.length())
            return 1;

        if (i == s.length())
            return 0;

        if (dp[i][j] != -1)
            return dp[i][j];

        int ret = numDistinct(s, t, i + 1, j);
        if (s.charAt(i) == t.charAt(j))
            ret += numDistinct(s, t, i + 1, j + 1);

        dp[i][j] = ret;
        return ret;
    }
}
