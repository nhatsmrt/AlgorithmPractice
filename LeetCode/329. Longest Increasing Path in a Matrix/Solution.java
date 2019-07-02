class Solution {
    private int[][] increase;

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0)
            return 0;
        increase = new int[matrix.length][matrix[0].length];

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                increase[i][j] = -1;
            }
        }

        int curMax = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                int candidate = longestIncreasingFrom(matrix, i, j);
                curMax = Math.max(curMax, candidate);
            }
        }

        return curMax;
    }

    private int longestIncreasingFrom(int[][] matrix, int i, int j) {
        if (increase[i][j] >= 0)
            return increase[i][j];

        int curMax = 0;
        if (i > 0 && matrix[i - 1][j] > matrix[i][j])
            curMax = Math.max(curMax, longestIncreasingFrom(matrix, i - 1, j));

        if (i < matrix.length - 1 && matrix[i + 1][j] > matrix[i][j])
            curMax = Math.max(curMax, longestIncreasingFrom(matrix, i + 1, j));


        if (j > 0 && matrix[i][j - 1] > matrix[i][j])
            curMax = Math.max(curMax, longestIncreasingFrom(matrix, i, j - 1));

        if (j < matrix[0].length - 1 && matrix[i][j + 1] > matrix[i][j])
            curMax = Math.max(curMax, longestIncreasingFrom(matrix, i, j + 1));

        increase[i][j] = curMax + 1;
        return curMax + 1;
    }


    private void printArray(int[][] arr) {
        String rep = "[";
        for (int i = 0; i < arr.length; i++) {
            String subarr = "[";
            for (int j = 0; j < arr[0].length; j++) {
                subarr += arr[i][j];
                if (j < arr[0].length - 1)
                    subarr += ", ";
            }
            subarr += "]";
            rep += "" + subarr;
            if (i < arr.length - 1)
                rep += ", ";
        }
        rep += "]";
        System.out.println(rep);
    }
}
