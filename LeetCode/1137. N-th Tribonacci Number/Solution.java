class Solution {
    public int tribonacci(int n) {
        if (n == 0)
            return 0;
        if (n <= 2)
            return 1;

        int[][] mat = matrixPower(n - 2);
        return mat[2][1] + mat[2][2];
    }

    private int[][] matrixPower(int n) {
        int pow = 0;
        while (1 << (pow + 1) <= n)
            pow += 1;

        int[][] mat = new int[3][3];
        mat[0][1] = mat[1][2] = mat[2][0] = mat[2][1] = mat[2][2] = 1;
        int[][] ret = new int[3][3];
        ret[0][0] = ret[1][1] = ret[2][2] = 1;

        for (int i = 0; i <= pow; i++) {
            if (i > 0)
                mat = matmul(mat, mat);

            if ((n & (1 << i)) > 0)
                ret = matmul(ret, mat);
        }
        return ret;
    }

    private void printMatrix(int[][] matrix) {
        System.out.print("[");
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++) {
                System.out.print(matrix[i][j]);
                if (j < matrix.length - 1)
                    System.out.print(", ");
            }
            if (i == matrix.length - 1)
                System.out.print("]");
            System.out.println();
        }
    }

    private int[][] matmul(int[][] matrix1, int[][] matrix2) {
        int[][] ret = new int[matrix1.length][matrix2[0].length];
        for (int i = 0; i < ret.length; i++) {
            for (int j = 0; j < ret[0].length; j++) {
                for (int k = 0; k < matrix1[0].length; k++)
                    ret[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }

        return ret;
    }
}
