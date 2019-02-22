class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix.length == 0)
            return 0;

        int[][] maximalSquareDP = new int[matrix.length][matrix[0].length];
        int ret = 0;

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == '0')
                    maximalSquareDP[i][j] = 0;
                else if (i == 0 || j == 0)
                    maximalSquareDP[i][j] = 1;
                else
                    maximalSquareDP[i][j] = min(
                        maximalSquareDP[i - 1][j],
                        maximalSquareDP[i][j - 1],
                        maximalSquareDP[i - 1][j - 1]
                    ) + 1;


                if (maximalSquareDP[i][j] > ret)
                    ret = maximalSquareDP[i][j];
            }
        }

        return ret * ret;
    }

    private int min(int a, int b, int c) {
        if (a <= b && a <= c)
            return a;
        else if (b <= a && b <= c)
            return b;
        else
            return c;
    }
}
