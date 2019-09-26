class Solution {
    public int[] sortArrayByParity(int[] A) {
        int lower = 0;
        int faster = 0;

        while (faster < A.length) {
            if (A[faster] % 2 == 0) {
                int tmp = A[lower];
                A[lower] = A[faster];
                A[faster] = tmp;
                lower += 1;
            }
            faster += 1;
        }

        return A;
    }
}
