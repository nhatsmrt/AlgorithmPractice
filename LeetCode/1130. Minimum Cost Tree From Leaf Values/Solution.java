class Solution {
    private int[][] dp;
    private int[][] cost;

    public int mctFromLeafValues(int[] arr) {
        // dp[i][j] = best result of subarray from i to j (inclusive)
        // dp[i][i] = 0; dp[i][i + 1] = arr[i] * arr[i + 1]
        // dp[i][j] = max_k (max(arr[i], ..., a[k]) * max(arr[k + 1], ..., a[j]) +
        //             + dp[i][k] + dp[k + 1][j])
        // cost[i][j] = max(arr[i], ..., a[j])
        // Solving both using DP
        // Time Complexity: O(n^2)

        cost = new int[arr.length][arr.length];
        dp = new int[arr.length][arr.length];
        for (int[] subarr : dp)
            Arrays.fill(subarr, -1);
        for (int[] subarr : cost)
            Arrays.fill(subarr, -1);
        return mctFromLeafValues(arr, 0, arr.length - 1);
    }

    private int mctFromLeafValues(int[] arr, int i, int j) {
        if (i == j)
            return 0;
        if (dp[i][j] != -1)
            return dp[i][j];

        int ret = -1;
        for (int k = i; k < j; k++) {
            int candidate = findMax(arr, i, k) * findMax(arr, k + 1, j)
                + mctFromLeafValues(arr, i, k) + mctFromLeafValues(arr, k + 1, j);
            if (ret == - 1 || ret > candidate)
                ret = candidate;
        }

        dp[i][j] = ret;
        return ret;
    }

    private int findMax(int[] arr, int i, int j) {
        if (i == j)
            return arr[i];
        if (cost[i][j] != -1)
            return cost[i][j];
        int ret = Math.max(findMax(arr, i, j - 1), arr[j]);
        cost[i][j] = ret;
        return ret;
    }
}
