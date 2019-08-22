class Solution {
    public int firstMissingPositive(int[] nums) {
        if (nums.length == 0)
            return 1;

        int i = 0;
        int n = 0;
        while (i < nums.length) {
            n = nums[i];
            if (n > 0 && n < nums.length + 1) {
                if (n != i + 1 && nums[n - 1] != n) {
                    int tmp = nums[i];
                    nums[i] = nums[n - 1];
                    nums[n - 1] = tmp;
                }
                else
                    i += 1;
            }
            else
                i += 1;
        }
        for (i = 0; i < nums.length; i++) {
            if (nums[i] != i + 1)
                return i + 1;
        }

        return nums.length + 1;
    }
}
