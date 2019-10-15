class Solution2 {
    private int[][][] dp;

    public int minDominoRotations(int[] A, int[] B) {
        if (A.length <= 1)
            return 0;
        int candidate1 = minDominoRotations(A, B, A[0]);
        int candidate2 = minDominoRotations(A, B, B[0]);

        if (candidate1 == -1)
            return candidate2;

        if (candidate2 == -1)
            return candidate1;

        return Math.min(candidate1, candidate2);
    }

    private int minDominoRotations(int[] A, int[] B, int first) {
        int rotationA = 0;
        int rotationB = 0;

        for (int i = 0; i < A.length; i++) {
            if (A[i] != first && B[i] != first)
                return -1;

            if (A[i] != first)
                rotationA += 1;
            if (B[i] != first)
                rotationB += 1;
        }

        return Math.min(rotationA, rotationB);
    }
}
