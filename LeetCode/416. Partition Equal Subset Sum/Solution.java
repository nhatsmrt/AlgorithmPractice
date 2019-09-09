class Solution {
    // O(sum * n) solution (pseudolinear)
    private int[][] dp;

    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++)
            sum += nums[i];

        if (sum % 2 != 0)
            return false;

        dp = new int[sum / 2][nums.length];
        return canPartition(nums, sum / 2, 0);
    }

    private boolean canPartition(int[] nums, int remaining, int ind) {
        if (remaining == 0)
            return true;
        if (remaining < 0)
            return false;
        if (dp[remaining - 1][ind] != 0)
            return dp[remaining - 1][ind] == 1;

        boolean ret = false;
        if (ind == nums.length - 1)
            ret = remaining == nums[ind];
        else
            ret = canPartition(nums, remaining - nums[ind], ind + 1) || canPartition(nums, remaining, ind + 1);

        if (ret)
            dp[remaining - 1][ind] = 1;
        else
            dp[remaining - 1][ind] = 2;
        return ret;
    }
}
