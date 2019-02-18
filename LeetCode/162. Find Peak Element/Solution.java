class Solution {
    public int findPeakElement(int[] nums) {
        if (nums.length == 1)
            return 0;

        return findPeak(nums, 0, nums.length - 1);

    }

    private int findPeak(int [] nums, int start, int end) {
        if (start == end)
            return start;

        int mid = (start + end) / 2;
        if (checkPeak(nums, mid))
            return mid;

        if (mid > start && nums[mid] < nums[mid - 1])
            return findPeak(nums, start, mid);
        else if (mid == start)
            return end;

        return findPeak(nums, mid, end);

    }


    private boolean checkPeak(int [] nums, int ind) {
        if (ind == 0)
            return nums[ind] > nums[1];

        if (ind == nums.length - 1)
            return nums[ind] > nums[ind - 1];


        return nums[ind] > nums[ind - 1] && nums[ind] > nums[ind + 1];
    }
}
