class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0)
            return false;
        return searchMatrix(matrix, target, 0, matrix.length * matrix[0].length - 1);
    }

    private boolean searchMatrix(int[][] matrix, int target, int start, int end) {
        if (start >= end)
            return get(matrix, start) == target;
        int mid = start + (end - start) / 2;
        int midVal = get(matrix, mid);
        if (midVal == target)
            return true;
        else if (midVal < target)
            return searchMatrix(matrix, target, mid + 1, end);

        return searchMatrix(matrix, target, start, mid - 1);
    }

    private int get(int[][] matrix, int ind) {
        int row = ind / matrix[0].length;
        int column = ind % matrix[0].length;
        return matrix[row][column];
    }
}
