class Solution {
    private List<Map<Integer, Integer>> indices;
    private int[][] dp;

    public int longestArithSeqLength(int[] A) {
        // Time and Space Complexity: O(N^2)

        indices = new ArrayList<>();

        for (int i = 0; i < A.length; i++)
            indices.add(new HashMap<>());

        indices.get(A.length - 1).put(A[A.length - 1], A.length - 1);
        for (int i = A.length - 2; i >= 0; i--) {
            for (int val : indices.get(i + 1).keySet())
                indices.get(i).put(val, indices.get(i + 1).get(val));

            indices.get(i).put(A[i], i);
        }

        dp = new int[A.length][A.length];

        int ret = 0;

        for (int i = 0; i < A.length; i++) {
            for (int j = i + 1; j < A.length; j++) {
                ret = Math.max(ret, 1 + longestAP(A, i, j));
            }
        }

        return ret;

    }

    private int longestAP(int[] A, int i, int j) {
        if (dp[i][j] > 0)
            return dp[i][j];
        else {
            int next = 2 * A[j] - A[i];
            int ret = 1;

            if (j + 1 < A.length && indices.get(j + 1).containsKey(next))
                ret += longestAP(A, j, indices.get(j + 1).get(next));

            dp[i][j] = ret;

            return ret;
        }
    }
}
