class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1)
            return 0;

        boolean findPeak = false;
        boolean foundBoth = true;
        int i = 0;
        int ret = 0;
        int low = 0;
        while (i < prices.length) {
            if (findPeak) {
                if (prices[i] > prices[i - 1] && (i == prices.length - 1 || prices[i] >= prices[i + 1])) {
                    findPeak = false;
                    ret += prices[i] - low;
                }
            }
            else {
                if ((i == 0 || prices[i] <= prices[i - 1]) && (i == prices.length - 1 || prices[i] < prices[i + 1])) {
                    low = prices[i];
                    findPeak = true;
                }
            }
            i += 1;
        }
        return ret;

    }
}
