class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 0)
            return -1;

        if (nums[0] < nums[nums.length - 1] || nums.length == 1) {
            int ret = Arrays.binarySearch(nums, target);
            if (ret < 0)
                return -1;
            else
                return ret;
        }

        int minInd = findMinInd(nums, 0, nums.length - 1);

        int candidate = -1;
        if (target <= nums[nums.length - 1])
            candidate = Arrays.binarySearch(nums, minInd, nums.length, target);
        else
            candidate = Arrays.binarySearch(nums, 0, minInd, target);

        return candidate >= 0 ? candidate : -1;
    }

    private int findMinInd(int[] nums, int start, int end) {
        if (start == end)
            return start;
        if (start + 1 == end)
            return nums[start] < nums[end] ? start : end;

        int mid = (end + start) / 2;
        if (nums[mid] < nums[mid + 1] && nums[mid - 1] > nums[mid])
            return mid;

        if (nums[start] > nums[mid])
            return findMinInd(nums, start, mid);
        else
            return findMinInd(nums, mid, end);
    }
}
