class Solution {
    public void nextPermutation(int[] nums) {
        int left = nums.length - 1;
        while (left > 0 && nums[left - 1] >= nums[left]) {
            left -= 1;
        }


        if (left == 0) {
            reverse(nums, 0, nums.length - 1);
        }
        else {
            int right = nums.length - 1;
            while (nums[left - 1] >= nums[right])
                right -= 1;

            swap(nums, left - 1, right);
            reverse(nums, left, nums.length - 1);
        }
    }

    private void reverse(int[] nums, int i, int j) {
        if (j > i) {
            swap(nums, i, j);
            reverse(nums, i + 1, j - 1);
        }
    }

    private void swap(int[] nums, int i, int j) {
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
    }
}
