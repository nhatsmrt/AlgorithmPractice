class NumMatrix {
    private int[][] cache;

    public NumMatrix(int[][] matrix) {
        if (matrix.length > 0) {
            cache = new int[matrix.length][matrix[0].length];
            cache[0][0] = matrix[0][0];

            for (int i = 1; i < matrix.length; i++)
                cache[i][0] = cache[i - 1][0] + matrix[i][0];

            for (int j = 1; j < matrix[0].length; j++)
                cache[0][j] = cache[0][j - 1] + matrix[0][j];

            for (int i = 1; i < matrix.length; i++) {
                for (int j = 1; j < matrix[0].length; j++)
                    cache[i][j] = cache[i - 1][j] + cache[i][j - 1] - cache[i - 1][j - 1] + matrix[i][j];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int ret = cache[row2][col2];

        if (row1 > 0)
            ret -= cache[row1 - 1][col2];
        if (col1 > 0)
            ret -= cache[row2][col1 - 1];

        if (row1 > 0 && col1 > 0)
            ret += cache[row1 - 1][col1 - 1];

        return ret;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
