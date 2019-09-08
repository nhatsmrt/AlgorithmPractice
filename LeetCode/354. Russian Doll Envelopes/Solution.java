class Solution {
    private int[] dp;

    public int maxEnvelopes(int[][] envelopes) {
        Arrays.sort(envelopes, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0], o2[0]);
            }
        });

        int curMax = 0;
        dp = new int[envelopes.length];
        Arrays.fill(dp, 1);
        for (int i = 0; i < envelopes.length; i++) {
            for (int j = i; j < envelopes.length; j++) {
                if (envelopes[i][0] < envelopes[j][0] && envelopes[i][1] < envelopes[j][1])
                    dp[j] = (int) Math.max(dp[j], dp[i] + 1);
            }
            if (curMax < dp[i])
                curMax = dp[i];
        }

        return curMax;
    }

}
