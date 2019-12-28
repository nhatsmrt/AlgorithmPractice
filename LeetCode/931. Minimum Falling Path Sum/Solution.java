class Solution {
    public int minFallingPathSum(int[][] A) {
        for (int i = A.length - 2; i >= 0; i--) {
            for (int j = 0; j < A[0].length; j++) {
                if (j == 0)
                    A[i][j] += Math.min(A[i + 1][j], A[i + 1][j + 1]);
                else if (j == A[0].length - 1)
                    A[i][j] += Math.min(A[i + 1][j], A[i + 1][j - 1]);
                else
                    A[i][j] += Math.min(
                        A[i + 1][j], Math.min(A[i + 1][j - 1], A[i + 1][j + 1])
                );
            }
        }

        int ret = A[0][0];
        for (int j = 1; j < A[0].length; j++) {
            if (A[0][j] < ret)
                ret = A[0][j];
        }

        return ret;
    }
}
