class Solution {
    public int fixedPoint(int[] A) {
        return fixedPoint(A, 0, A.length - 1);
    }

    private int fixedPoint(int[] A, int i, int j) {
        if (A[i] - i == 0)
            return i;

        if (i >= j)
            return -1;

        int mid = i + (j - i) / 2;
        if (A[mid] - mid > 0)
            return fixedPoint(A, i + 1, mid - 1);
        else if (A[mid] - mid == 0)
            return fixedPoint(A, i + 1, mid);
        else
            return fixedPoint(A, mid + 1, j);
    }
}
