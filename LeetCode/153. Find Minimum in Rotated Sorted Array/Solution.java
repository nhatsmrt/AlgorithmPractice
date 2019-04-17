class Solution {
    public int findMin(int[] nums) {
        if (nums.length == 1)
            return nums[0];

        if (nums[0] < nums[nums.length - 1])
            return nums[0];

        return nums[findMinInd(nums, 0, nums.length - 1)];
    }

    private int findMinInd(int[] nums, int start, int end) {
        if (start == end)
            return start;

        if (end == start + 1)
            return nums[start] < nums[end] ? start : end;

        int mid = (start + end) / 2;
        if (
            (mid == nums.length - 1 || nums[mid] < nums[mid + 1]) &&
            (mid == 0 || nums[mid] < nums[mid - 1])
        )
            return mid;


        if (nums[start] > nums[mid])
            return findMinInd(nums, start, mid);
        else
            return findMinInd(nums, mid, end);
    }
}
