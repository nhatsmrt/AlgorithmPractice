class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        if (matrix.length == 0)
            return new ArrayList<Integer>();

        return spiralRecursion(matrix, 0, matrix.length - 1, 0, matrix[0].length - 1);
    }

    private List<Integer> spiralRecursion(int[][] matrix, int up, int down, int left, int right) {
        List<Integer> ret = new ArrayList<Integer>();

        if (up > down || left > right)
            return ret;

        // 1 row:
        if (up == down) {
            for (int j = left; j <= right; j++) {
                ret.add(matrix[up][j]);
            }
            return ret;
        }

        // 1 column:
        if (left == right) {
            for (int i = up; i <= down; i++) {
                ret.add(matrix[i][right]);
            }
            return ret;
        }


        for (int j = left; j <= right; j++) {
            ret.add(matrix[up][j]);
        }

        for (int i = up + 1; i <= down; i++) {
            ret.add(matrix[i][right]);
        }

        for (int j = right - 1; j >= left; j--) {
            ret.add(matrix[down][j]);
        }

        for (int i = down - 1; i >= up + 1; i--) {
            ret.add(matrix[i][left]);
        }

        List<Integer> inner = spiralRecursion(matrix, up + 1, down - 1, left + 1, right - 1);
        ret.addAll(inner);
        return ret;
    }
}
