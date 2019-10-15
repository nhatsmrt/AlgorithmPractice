class Solution {
    private int[][][] dp;

    public int minDominoRotations(int[] A, int[] B) {
        if (A.length <= 1)
            return 0;

        dp = new int[A.length][2][2];
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < 2; j++)
                dp[i][j][0] = dp[i][j][1] = -1;
        }


        List<Integer> candidates = new ArrayList<Integer>();
        int candidate1 = minDominoRotations(A, B, 1, 0, 0);
        if (candidate1 > -1)
            candidates.add(candidate1);

        int candidate2 = minDominoRotations(A, B, 1, 1, 1);
        if (candidate2 > -1)
            candidates.add(candidate2);

        int candidate3 = minDominoRotations(A, B, 1, 1, 0);
        if (candidate3 > -1) {
            candidate3 += 1;
            candidates.add(candidate3);
        }

        int candidate4 = minDominoRotations(A, B, 1, 0, 1);
        if (candidate4 > -1) {
            candidate4 += 1;
            candidates.add(candidate4);
        }
        int ret = -1;
        for (int i = 0; i < candidates.size(); i++) {
            if (candidates.get(i) < ret || ret == -1)
                ret = candidates.get(i);
        }
        return ret;
    }

    private int minDominoRotations(
        int[] A, int[] B,
        int pos, int prev, int row
    ) {
        if (pos == A.length)
            return 0;


        if (dp[pos][prev][row] != -1)
            return dp[pos][prev][row];

        int first = A[0];
        if (prev == 1)
            first = B[0];

        int ret = -1;
        if (A[pos] == first || B[pos] == first) {
            int next = minDominoRotations(A, B, pos + 1, prev, row);
            if (next != -1) {
                if (row == 0) {
                    if (A[pos] == first)
                        ret = next;
                    else if (B[pos] == first)
                        ret = 1 + next;
                }
                else {
                    if (B[pos] == first)
                        ret = next;
                    else if (A[pos] == first)
                        ret = 1 + next;
                }
            }
        }

        dp[pos][prev][row] = ret;
        return ret;
    }
}
