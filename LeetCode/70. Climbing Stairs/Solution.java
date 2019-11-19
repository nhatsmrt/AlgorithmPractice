class Solution {
    public int climbStairs(int n) {
        // O(log n) solution

        if (n == 1)
            return 1;

        int[][] mat = pow(n - 1);
        return mat[1][0] + mat[1][1];
    }

    private int[][] pow(int n) {
        int[][] mat = new int[2][2];
        int[][] ret = new int[2][2];
        ret[0][0] = ret[1][1] = 1;
        mat[0][1] = mat[1][0] = mat[1][1] = 1;

        int i = 1;
        while (i <= n) {
            if ((n & i) > 0)
                ret = multiply(ret, mat);

            i *= 2;
            mat = multiply(mat, mat);
        }

        return ret;
    }

    private int[][] multiply(int[][] mat1, int[][] mat2) {
        int[][] ret = new int[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++)
                    ret[i][j] += mat1[i][k] * mat2[k][j];
            }
        }

        return ret;
    }
}
