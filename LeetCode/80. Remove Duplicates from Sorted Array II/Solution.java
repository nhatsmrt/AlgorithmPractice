class Solution {
    public int removeDuplicates(int[] nums) {
        int cur = 1;

        for (int check = 1; check < nums.length; check++) {
            if (nums[check] != nums[cur - 1] || (cur == 1 || nums[check] != nums[cur - 2])) {
                nums[cur] = nums[check];
                cur += 1;
            }
        }

        return cur;
    }
}
