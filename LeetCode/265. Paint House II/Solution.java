class Solution {
    private int[][] dp;
    private int[][] argmin2;

    public int minCostII(int[][] costs) {
        if (costs.length == 0)
            return 0;

        dp = new int[costs.length][costs[0].length];

        argmin2 = new int[costs.length][3];
        if (costs[0].length > 2) {
            for (int i = 0; i < costs.length; i++) {
                int min1 = -1;
                int min2 = -1;
                int min3 = -1;

                for (int j = 0; j < costs[0].length; j++) {
                    if (min1 == -1 || costs[i][j] < costs[i][min1])
                        min1 = j;
                }

                for (int j = 0; j < costs[0].length; j++) {
                    if (j != min1 && (min2 == -1 || costs[i][j] < costs[i][min2]))
                        min2 = j;
                }

                for (int j = 0; j < costs[0].length; j++) {
                    if (j != min1 && j!= min2 && (min3 == -1 || costs[i][j] < costs[i][min3]))
                        min3 = j;
                }

                argmin2[i][0] = min1;
                argmin2[i][1] = min2;
                argmin2[i][2] = min3;
            }
        }

        for (int i = 0; i < costs.length; i++)
            Arrays.fill(dp[i], -1);


        int ret = -1;
        for (int k = 0; k < costs[0].length; k++) {
            if (ret == -1 || ret > minCostII(costs, 0, k))
                ret = minCostII(costs, 0, k);
        }
        return ret;

    }

    private int minCostII(int[][] costs, int house, int color) {
        if (dp[house][color] != -1)
            return dp[house][color];

        int ret = costs[house][color];
        if (house < costs.length - 1) {
            int remaining = -1;
            if (costs[0].length <= 2) {
                for (int k = 0; k < costs[0].length; k++) {
                    if (
                        k != color &&
                        (remaining == -1 || remaining > minCostII(costs, house + 1, k))
                    )
                        remaining = minCostII(costs, house + 1, k);
                }
            }
            else {
                int candidate1 = minCostII(costs, house + 1, argmin2[house + 1][0]);
                int candidate2 = minCostII(costs, house + 1, argmin2[house + 1][1]);
                int candidate3 = minCostII(costs, house + 1, argmin2[house + 1][2]);
                if (color != argmin2[house + 1][0] && color != argmin2[house + 1][1])
                    remaining = Math.min(candidate1, candidate2);
                else if (color == argmin2[house + 1][0])
                    remaining = Math.min(candidate2, candidate3);
                else
                    remaining = Math.min(candidate1, candidate3);
            }

            ret += remaining;
        }


        dp[house][color] = ret;
        return ret;
    }

}
