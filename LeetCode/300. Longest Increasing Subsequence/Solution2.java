class Solution2 {
    // O(n log n) solution
    public int lengthOfLIS(int[] nums) {
        int[] initial = new int[nums.length];
        int curLen = 0;

        for (int i = nums.length - 1; i >= 0; i--) {
            int insertPoint = Arrays.binarySearch(initial, 0, curLen, -nums[i]);
            if (insertPoint < 0)
                insertPoint = -insertPoint - 1;
            initial[insertPoint] = -nums[i];
            if (insertPoint == curLen) {
                curLen += 1;
            }
        }

        return curLen;
    }
}
