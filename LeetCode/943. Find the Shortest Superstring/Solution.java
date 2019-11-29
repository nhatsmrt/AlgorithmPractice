class Solution {
    private int[][] cost;
    private int[][][] dp;


    public String shortestSuperstring(String[] A) {
        // Time Complexity: O(N^2 (2^N + W^2))
        // Space Complexity: O(N2^N)

        cost = new int[A.length][A.length];
        for (int i = 0; i < A.length; i++) {
            for (int j = i + 1; j < A.length; j++) {
                cost[i][j] = computeDistance(A[i], A[j]);
                cost[j][i] = computeDistance(A[j], A[i]);
            }
        }

        // dp[i][state] = min_{j in subset} cost[i][j] + dp[j][new state]
        int maxState = 1 << A.length;
        dp = new int[A.length][maxState][2];
        int minLen = -1;
        int start = -1;


        for (int i = 0; i < A.length; i++)
            dp[i][0][0] = A[i].length();

        for (int i = 0; i < A.length; i++) {
            int candidate = shortestSuperString(i, maxState - (1 << i) - 1);
            if (minLen == -1 || candidate < minLen) {
                minLen = candidate;
                start = i;
            }
        }

        int state = maxState - 1 - (1 << start);
        int from = 0;
        StringBuffer ret = new StringBuffer();

        for (int i = 0; i < A.length; i++) {
            ret.append(A[start].substring(from));
            from = (A[start].length() - cost[start][dp[start][state][1]]);

            start = dp[start][state][1];
            state -= 1 << start;
        }

        return ret.toString();
    }

    private int shortestSuperString(int i, int state) {
        if (dp[i][state][0] != 0)
            return dp[i][state][0];

        int ret = -1;
        int next = -1;

        int chosen = 0;
        int code = 1 << chosen;

        while (code <= state) {
            if (i != chosen && (state & code) > 0) {
                int candidate = cost[i][chosen] + shortestSuperString(chosen, state - code);
                if (ret == -1 || candidate < ret) {
                    ret = candidate;
                    next = chosen;
                }
            }

            chosen += 1;
            code = 1 << chosen;
        }

        dp[i][state][0] = ret;
        dp[i][state][1] = next;
        return ret;
    }

    private int computeDistance(String str1, String str2) {
        int it1 = 1;

        while (str2.indexOf(str1.substring(it1)) != 0)
            it1 += 1;
        return it1;
    }
}
