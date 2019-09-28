class Solution {
    public int distinctSubseqII(String S) {
        if (S.length() < 2)
            return S.length();

        int[] dp = new int[S.length() + 1];
        int[] last = new int[26];
        Arrays.fill(last, -1);
        dp[0] = 1;
        
        for (int i = 1; i <= S.length(); i++) {
            dp[i] = (2 * dp[i - 1]) % 1000000007;
            if (last[S.charAt(i - 1) - 'a'] != -1) {
                dp[i] -= dp[last[S.charAt(i - 1) - 'a'] - 1];
                dp[i] %= 1000000007;
            }
            last[S.charAt(i - 1) - 'a'] = i;
        }

        dp[S.length()] -= 1;
        if (dp[S.length()] < 0)
            dp[S.length()] += 1000000007;
        return dp[S.length()];
    }
}
