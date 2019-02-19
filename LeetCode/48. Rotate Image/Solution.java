class Solution {
    public void rotate(int[][] matrix) {
        transposeSubmatrix(matrix, 0);

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length / 2; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix.length - 1 - j];
                matrix[i][matrix.length - 1 - j] = tmp;
            }
        }
    }

    private void transposeSubmatrix(int[][] matrix, int m) {
        if (m != matrix.length - 1) {
            for (int i = m; i < matrix.length; i++) {
                int tmp = matrix[i][m];
                matrix[i][m] = matrix[m][i];
                matrix[m][i] = tmp;
            }
            transposeSubmatrix(matrix, m + 1);
        }
    }
}
