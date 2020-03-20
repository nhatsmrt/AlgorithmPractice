class NumMatrix {
    // 2D Fenwick Tree
    // O(mn) build, O(log(m)log(n)) per query
    private int[][] data;

    public NumMatrix(int[][] matrix) {
        if (matrix.length > 0 && matrix[0].length > 0) {
            data = new int[matrix.length + 1][matrix[0].length + 1];
            int[][] prefixes = new int[matrix.length + 1][matrix[0].length + 1];

            for (int i = 1; i <= matrix.length; i++) {
                for (int j = 1; j <= matrix[0].length; j++) {
                    prefixes[i][j] = prefixes[i - 1][j] + prefixes[i][j - 1]
                        - prefixes[i - 1][j - 1] + matrix[i - 1][j - 1];
                    data[i][j] = prefixes[i][j] - prefixes[i][j - lastSetBit(j)]
                    -prefixes[i - lastSetBit(i)][j] + prefixes[i - lastSetBit(i)][j - lastSetBit(j)];
                }
            }
        }
    }

    public void update(int row, int col, int val) {
        int oldVal = sumRegion(row, col, row, col);
        increment(row + 1, col + 1, val - oldVal);
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix(row2 + 1, col2 + 1) - prefix(row1, col2 + 1)
            - prefix(row2 + 1, col1) + prefix(row1, col1);
    }

    private void increment(int i, int j, int delta) {
        while (i < data.length) {
            int jIt = j;

            while (jIt < data[0].length) {
                data[i][jIt] += delta;
                jIt += lastSetBit(jIt);
            }

            i += lastSetBit(i);
        }
    }

    private int prefix(int i, int j) {
        int ret = 0;

        while (i > 0) {
            int jIt = j;

            while (jIt > 0) {
                ret += data[i][jIt];
                jIt -= lastSetBit(jIt);
            }

            i -= lastSetBit(i);
        }

        return ret;
    }

    private int lastSetBit(int ind) {
        return ind & (-ind);
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * obj.update(row,col,val);
 * int param_2 = obj.sumRegion(row1,col1,row2,col2);
 */
