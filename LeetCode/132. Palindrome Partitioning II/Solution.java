
class Solution {
    private int[] dp;
    private boolean[][] isPalindrome;

    public int minCut(String s) {
        dp = new int[s.length() + 1];
        isPalindrome = new boolean[s.length()][s.length()];
        // dp[i] = palindromic length of s[:i]
        // dp[i] = min_{j = 0, 1, ..., i} dp[j] + 1 given s[j : i] is a palindrome
        // Time complexity: O(n^2)
        // Space complexity: O(n^2)

        for (int i = 0; i < s.length(); i++) {
            int start = i;
            int end = i;

            while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
                isPalindrome[start][end] = true;
                start -= 1;
                end += 1;
            }

            if (i > 0) {
                start = i - 1;
                end = i;

                while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
                    isPalindrome[start][end] = true;
                    start -= 1;
                    end += 1;
                }
            }
        }


        Arrays.fill(dp, -1);
        dp[0] = 0;
        return minCut(s, s.length()) - 1;
    }

    private int minCut(String s, int i) {
        if (dp[i] != -1)
            return dp[i];

        int ret = minCut(s, i - 1) + 1;
        for (int j = i - 2; j >= 0; j--) {
            if (isPalindrome[j][i - 1]) {
                int candidate = minCut(s, j) + 1;
                if (candidate < ret)
                    ret = candidate;
            }
        }

        dp[i] = ret;
        return ret;
    }
}
