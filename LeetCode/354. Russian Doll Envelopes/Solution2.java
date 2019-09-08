class Solution2 {
  // O(n log n) solution
    public int maxEnvelopes(int[][] envelopes) {
        Arrays.sort(envelopes, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                int check1 = Integer.compare(o1[0], o2[0]);
                if (check1 != 0)
                    return check1;
                else
                    return -Integer.compare(o1[1], o2[1]);
            }
        });

        int[] nums = new int[envelopes.length];
        for (int i = 0; i < envelopes.length; i++)
            nums[i] = envelopes[i][1];

        int[] initial = new int[nums.length];
        int curMax = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            int insertPoint = Arrays.binarySearch(initial, 0, curMax, -nums[i]);
            if (insertPoint < 0)
                insertPoint = -insertPoint - 1;

            if (insertPoint == curMax) {
                curMax += 1;
            }
            initial[insertPoint] = -nums[i];
        }

        return curMax;
    }

}
