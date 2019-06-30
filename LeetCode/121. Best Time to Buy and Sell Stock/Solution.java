class Solution {
    public int maxProfit(int[] prices) {
        int[] diff = new int[prices.length];
        for (int i = 0; i < prices.length - 1; i++) {
            diff[i] = prices[i + 1] - prices[i];
        }
        return maxContiguousSum(diff);
    }

    private int maxContiguousSum(int[] nums) {
        // Kadane's algorithm: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
        int curMax = 0;
        int maxEndingHere = 0;
        for (int i = 0; i < nums.length; i++) {
            maxEndingHere += nums[i];
            if (maxEndingHere < 0)
                maxEndingHere = 0;
            if (curMax < maxEndingHere)
                curMax = maxEndingHere;
        }
        return curMax;
    }
}
