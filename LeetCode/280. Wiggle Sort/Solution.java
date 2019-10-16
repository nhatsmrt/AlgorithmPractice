class Solution {
    public void wiggleSort(int[] nums) {
        int tmp;
        for (int i = 0; i < nums.length - 1; i++) {
            if (i % 2 == 0) {
                if (nums[i] > nums[i + 1]) {
                    tmp = nums[i];
                    nums[i] = nums[i + 1];
                    nums[i + 1] = tmp;
                }
            }
            else {
                if (nums[i] < nums[i + 1]) {
                    tmp = nums[i];
                    nums[i] = nums[i + 1];
                    nums[i + 1] = tmp;
                }
            }
        }
    }
}
