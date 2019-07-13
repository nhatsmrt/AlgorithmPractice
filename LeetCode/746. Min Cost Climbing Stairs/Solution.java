class Solution {
    public int minCostClimbingStairs(int[] cost) {
        for (int j = cost.length - 3; j >= 0; j--) {
            cost[j] += Math.min(cost[j + 1], cost[j + 2]);
        }

        return Math.min(cost[0], cost[1]);
    }
}
