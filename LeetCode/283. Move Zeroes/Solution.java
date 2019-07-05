class Solution {
    public void moveZeroes(int[] nums) {
        int firstZero = 0;
        while (firstZero < nums.length && nums[firstZero] != 0)
            firstZero += 1;
        if (firstZero < nums.length) {
            int i = firstZero + 1;
            while (i < nums.length) {
                if (nums[i] != 0) {
                    nums[firstZero] = nums[i];
                    nums[i] = 0;
                    firstZero += 1;
                }
                i += 1;
            }
        }
    }
}
