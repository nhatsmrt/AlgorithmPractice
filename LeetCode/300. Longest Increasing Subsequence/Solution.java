class Solution {
    int[] longestTo;
    public int lengthOfLISDP(int[] nums, int i) {
        if (longestTo[i] != -1)
            return longestTo[i];

        int ret = 1;
        int size = nums.length;
        int curMax = 0;
        int candidate = 0;

        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                candidate = lengthOfLISDP(nums, j);
                if (candidate > curMax)
                    curMax = candidate;
            }
        }

        ret += curMax;

        longestTo[i] = ret;
        return ret;
    }

    public int lengthOfLIS(int[] nums) {
        int size = nums.length;

        if (size < 2)
            return size;

        longestTo = new int[size];
        Arrays.fill(longestTo, -1);
        longestTo[0] = 1;

        int curMin = lengthOfLISDP(nums, size - 1);
        for (int i = size - 2; i >= 0; i--) {
            int candidate = lengthOfLISDP(nums, i);
            if (candidate > curMin)
                curMin = candidate;
        }

        return curMin;

    }
}
