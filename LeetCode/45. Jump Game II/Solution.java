class Solution {
    public int jump(int[] nums) {
        // Greedy, O(n) time complexity, O(1) space complexity
        int begin = 0;
        int end = nums[0];
        int maxJumpable = nums[0];
        int ret = 0;

        for (int i = 1; i < nums.length; i++) {
            if (end >= nums.length - 1) {
                ret += 1;
                break;
            }

            if (i + nums[i] >= nums.length - 1) {
                ret += 2;
                break;
            }

            if (i + nums[i] > maxJumpable)
                maxJumpable = i + nums[i];

            if (i == end) {
                end = maxJumpable;
                ret += 1;
            }
        }

        return ret;
    }

}
