class Solution {
    private Map<String, Integer> dp;

    public int lastStoneWeightII(int[] stones) {
        if (stones.length == 0)
            return 0;

        if (stones.length == 1)
            return stones[0];
        int sum = 0;
        for (int i = 0; i < stones.length; i++)
            sum += stones[i];

        dp = new HashMap<String, Integer>();

        return smallestWeight(stones, 0, 0);
    }

    public int smallestWeight(int[] stones, int i, int curWeight) {
        if (i == stones.length) {
            if (curWeight >= 0)
                return curWeight;

            return -2;
        }

        String key = i + "_" + curWeight;

        if (dp.containsKey(key))
            return dp.get(key);

        int ret = smallestWeight(stones, i + 1, curWeight + stones[i]);
        int candidate = smallestWeight(stones, i + 1, curWeight - stones[i]);

        if (candidate != -2) {
            ret = ret < candidate ? ret : candidate;
        }

        dp.put(key, ret);
        return ret;
    }

}
