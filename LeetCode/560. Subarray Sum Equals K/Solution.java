class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> prefixIndex = new HashMap<Integer, Integer>();
        int cumSum = 0;
        prefixIndex.put(0, 1);
        int ret = 0;

        for (int i = 1; i < nums.length + 1; i++) {
            cumSum += nums[i - 1];
            if (prefixIndex.containsKey(cumSum - k))
                ret += prefixIndex.get(cumSum - k);
            if (!prefixIndex.containsKey(cumSum))
                prefixIndex.put(cumSum, 0);
            prefixIndex.put(cumSum, prefixIndex.get(cumSum) + 1);

        }

        return ret;
    }
}
