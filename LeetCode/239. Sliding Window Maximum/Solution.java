class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0)
            return nums;

        int[] ret = new int[nums.length + 1 - k];
        int curIndMax = 0;

        for (int i = 1; i < k; i++) {
            if (nums[i] > nums[curIndMax]) {
                curIndMax = i;
            }
        }

        ret[0] = nums[curIndMax];
        int next = k;
        while (next < nums.length) {
            if (curIndMax > next - k) {
                if (nums[curIndMax] <= nums[next])
                    curIndMax = next;
            }
            else {
                curIndMax = next - k + 1;
                for (int i = next - k + 2; i <= next; i++) {
                    if (nums[i] > nums[curIndMax])
                        curIndMax = i;
                }
            }
            ret[next + 1 - k] = nums[curIndMax];
            next += 1;
        }

        return ret;
    }
}
