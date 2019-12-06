class Solution {
    public int wiggleMaxLength(int[] nums) {
        // Time complexity: O(n)
        // Space complexity: O(1)


        if (nums.length < 2)
            return nums.length;

        int prevDiff = nums[1] - nums[0];
        int ret = prevDiff != 0 ? 2 : 1;
        for (int i = 1; i < nums.length - 1; i++) {
            int diff = nums[i + 1] - nums[i];
            if ((diff > 0 && prevDiff <= 0) || (diff < 0 && prevDiff >= 0)) {
                ret += 1;
                prevDiff = diff;
            }
        }

        return ret;
    }
}
