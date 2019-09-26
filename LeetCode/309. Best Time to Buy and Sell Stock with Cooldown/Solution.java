class Solution {
    private int[][] dp;

    public int maxProfit(int[] prices) {
        dp = new int[prices.length][3];
        for (int i = 0; i < prices.length; i++)
            Arrays.fill(dp[i], -1);

        return maxProfit(prices, 0, 0);
    }

    private int maxProfit(int[] prices, int i, int status) {
        // status:
        // 0 = buyable, 1 = cooldown, 2 = bought

        if (i == prices.length)
            return 0;

        if (dp[i][status] != -1)
            return dp[i][status];

        int ret = 0;
        if (status == 1)
            ret = maxProfit(prices, i + 1, 0);
        else {
            int candidate1 = 0;
            int candidate2 = 0;
            if (status == 0) {
                candidate1 = maxProfit(prices, i + 1, 0);
                candidate2 = maxProfit(prices, i + 1, 2) - prices[i];
            }
            else {
                candidate1 = maxProfit(prices, i + 1, 2);
                candidate2 = maxProfit(prices, i + 1, 1) + prices[i];
            }

            ret = candidate1 > candidate2 ? candidate1 : candidate2;
        }

        dp[i][status] = ret;
        return ret;
    }
}
