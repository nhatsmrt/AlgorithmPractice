class Solution {
    private int[] dp;

    public int longestValidParentheses(String s) {
        if (s.length() < 2)
            return 0;
        dp = new int[s.length()];
        int curMax = 0;

        for (int i = dp.length - 1; i >= 0; i--) {
            int candidate = maxValidFrom(s, i);
            if (candidate > curMax)
                curMax = candidate;
        }
        return curMax;
    }

    private int maxValidFrom(String s, int start) {
        int ret = 0;
        if (start < s.length() - 1 && s.charAt(start) == '(') {
            int end = start + 1;

            if (dp[end] > 0)
                end += dp[end];

            if (end < s.length() && s.charAt(end) == ')') {
                end += 1;
                if (end < s.length() - 1)
                    end += dp[end];
                ret = end - start;
            }
        }

        dp[start] = ret;
        return ret;
    }
}
