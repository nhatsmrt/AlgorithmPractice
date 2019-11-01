class Solution {
    private int[][] dp;

    public int minCost(int[][] costs) {
        if (costs.length == 0)
            return 0;

        dp = new int[costs.length][3];
        for (int i = 0; i < costs.length; i++)
            dp[i][0] = dp[i][1] = dp[i][2] = -1;

        int ret = Math.min(
            minCost(costs, 0, 0),
            Math.min(minCost(costs, 0, 1), minCost(costs, 0, 2))
        );

        return ret;
    }

    private int minCost(int[][] costs, int house, int color) {
        if (dp[house][color] != -1)
            return dp[house][color];

        int ret = costs[house][color];
        if (house < costs.length - 1) {
            int color1 = (color + 1) % 3;
            int color2 = (color + 2) % 3;
            int candidate1 = minCost(costs, house + 1, color1);
            int candidate2 = minCost(costs, house + 1, color2);
            ret += candidate1 < candidate2 ? candidate1 : candidate2;
        }

        dp[house][color] = ret;
        return ret;
    }
}
