class Solution {
    public int maxSubArray(int[] nums) {
        // Kadane's algorithm: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

        if (nums.length == 0)
            return 0;
        if (nums.length == 1)
            return nums[0];

        int curMax = -100000;
        int maxEndingHere = -100000;
        for (int i = 0; i < nums.length; i++) {
            maxEndingHere += nums[i];
            if (maxEndingHere < nums[i])
                maxEndingHere = nums[i];
            if (curMax < maxEndingHere)
                curMax = maxEndingHere;
        }
        return curMax;
    }
}
