class Solution {
    private int[][][] dp;

    public int maxProfit(int k, int[] prices) {
        prices = reducedSize(prices);
        k = Math.min(prices.length / 2, k);

        dp = new int[prices.length][2][k];
        for (int i = 0; i < dp.length; i++) {
            for (int j = 0; j < k; j++)
                dp[i][0][j] = dp[i][1][j] = -1000000;
        }

        return maxProfit(prices, 0, 1, k);
    }

    private int maxProfit(int[] prices, int day, int buy, int remain) {
        if (remain == 0 || day == prices.length)
            return 0;

        if (dp[day][buy][remain - 1] != -1000000)
            return dp[day][buy][remain - 1];

        int ret = -1;
        if (buy == 0) {
            // currently holding

            // keep holding
            int candidate1 = maxProfit(prices, day + 1, buy, remain);

            // sell stock
            int candidate2 = prices[day] + maxProfit(prices, day + 1, 1 - buy, remain - 1);
            ret = candidate1 > candidate2 ? candidate1 : candidate2;
        }
        else {
            // not holding

            // ignore
            int candidate1 = maxProfit(prices, day + 1, buy, remain);

            // buy stock
            int candidate2 = -prices[day] + maxProfit(prices, day + 1, 1 - buy, remain);

            ret = candidate1 > candidate2 ? candidate1 : candidate2;
        }

        dp[day][buy][remain - 1] = ret;
        return ret;
    }

    private int[] reducedSize(int[] prices) {
        List<Integer> reducedPrices = new ArrayList<Integer>();
        boolean dec = true;
        int ind = 0;
        while (ind < prices.length) {
            if (dec) {
                if (ind == prices.length - 1 || prices[ind] < prices[ind + 1]) {
                    reducedPrices.add(prices[ind]);
                    dec = false;
                }
            }
            else {
                if (ind == prices.length - 1 || prices[ind] > prices[ind + 1]) {
                    reducedPrices.add(prices[ind]);
                    dec = true;
                }
            }

            ind += 1;
        }

        int[] ret = new int[reducedPrices.size()];
        for (int i = 0; i < ret.length; i++)
            ret[i] = reducedPrices.get(i);

        return ret;
    }
}
