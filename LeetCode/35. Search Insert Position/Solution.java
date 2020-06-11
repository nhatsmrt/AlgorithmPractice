class Solution {
    public int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length;

        while (low < high) {
            int mid = (low + high) / 2;

            if (nums[mid] >= target)
                high = mid;
            else
                low = mid + 1;
        }

        return low;
    }
}
