class Solution {
    private boolean searchMatrix(int[][] matrix, int l1, int r1, int l2, int r2, int target) {
        if (l1 > r1 || l2 > r2)
            return false;

        if (l1 == r1 && l2 == r2)
            return matrix[l1][l2] == target;


        int mid1 = (l1 + r1) / 2;
        int mid2 = (l2 + r2) / 2;

        if (matrix[mid1][mid2] == target)
            return true;
        else if (matrix[mid1][mid2] < target) {

            return searchMatrix(matrix, mid1 + 1, r1, l2, r2, target) ||
                   searchMatrix(matrix, l1, r1, mid2 + 1, r2, target);
        }
        else

            return searchMatrix(matrix, l1, mid1 - 1, l2, r2, target) ||
                   searchMatrix(matrix, l1, r1, l2, mid2 - 1, target);
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0)
            return false;
        else if (matrix[0].length == 0)
            return false;

        return searchMatrix(matrix, 0, matrix.length - 1, 0, matrix[0].length - 1, target);
    }
}
