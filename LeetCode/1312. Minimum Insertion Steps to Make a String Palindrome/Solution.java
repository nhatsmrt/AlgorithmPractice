class Solution {
    private int[][] dp;

    public int minInsertions(String s) {
        // O(n^2) time and space complexity
        dp = new int[s.length()][s.length()];
        for (int[] arr : dp)
            Arrays.fill(arr, -1);

        return minInsertions(s, 0, s.length() - 1);
    }

    private int minInsertions(String s, int start, int end) {
        if (start >= end)
            return 0;

        if (dp[start][end] != -1)
            return dp[start][end];

        int ret = 0;
        if (s.charAt(start) == s.charAt(end))
            ret = minInsertions(s, start + 1, end - 1);
        else {
            int candidate1 = minInsertions(s, start + 1, end);
            int candidate2 = minInsertions(s, start, end - 1);

            ret = candidate1 < candidate2 ? candidate1 : candidate2;
            ret += 1;
        }

        dp[start][end] = ret;
        return ret;
    }
}
