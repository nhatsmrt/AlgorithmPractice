class NumArray {
    private int[] prefix;

    public NumArray(int[] nums) {
        if (nums.length > 0) {
            prefix = new int[nums.length];
            prefix[0] = nums[0];

            for (int i = 1; i < nums.length; i++)
                prefix[i] = nums[i] + prefix[i - 1];
        }
    }

    public int sumRange(int i, int j) {
        if (i == 0)
            return prefix[j];
        else
            return prefix[j] - prefix[i - 1];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */
