class Solution {
    int size;
    public int searchFirst(int[] nums, int target, int start, int ind, int end) {
        if (start < 0 || end >= size || ind < start || ind > end)
            return -1;

        if (start == end) {
            if (nums[ind] == target)
                return ind;
            else
                return -1;
        }

        if (nums[ind] == target && (ind == 0 || nums[ind - 1] != target))
            return ind;

        if (nums[ind] < target) {
            if (ind == end)
                return -1;

            int newInd = (ind + end + 1) / 2;
            return searchFirst(nums, target, ind + 1, newInd, end);
        }

        // nums[ind] > target || nums[ind] == target && nums[ind - 1] == target
        if (ind == start)
            return -1;

        int newInd = (ind + start) / 2;
        return searchFirst(nums, target, start, newInd, ind - 1);
    }

    public int searchLast(int[] nums, int target, int start, int ind, int end) {
        // System.out.println(start);
        // System.out.println(ind);
        // System.out.println(end);

        if (start < 0 || end >= size || ind < start || ind > end)
            return -1;

        if (start == end) {
            if (nums[ind] == target)
                return ind;
            else
                return -1;
        }

        if (nums[ind] == target && (ind == size - 1 || nums[ind + 1] != target))
            return ind;

        if (nums[ind] > target) {
            if (ind == start)
                return -1;

            int newInd = (ind + start) / 2;
            return searchLast(nums, target, start, newInd, ind - 1);
        }

        // nums[ind] < target || nums[ind] == target && nums[ind + 1] == target
        if (ind == end)
            return -1;
        int newInd = (ind + end + 1) / 2;
        return searchLast(nums, target, ind + 1, newInd, end);
    }


    public int[] searchRange(int[] nums, int target) {
        int[] ret = new int[2];

        if (nums.length < 1) {
            ret[0] = -1;
            ret[1] = -1;
            return ret;
        }

        size = nums.length;
        int mid = size / 2;

        ret[0] = searchFirst(nums, target, 0, mid, size - 1);
        ret[1] = searchLast(nums, target, 0, mid, size - 1);

        return ret;
    }
}
