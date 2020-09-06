class Solution {
    public int largestOverlap(int[][] A, int[][] B) {
        int ret = 0;
        for (int dx = -A.length + 1; dx <= A.length -1; dx++) {
            for (int dy = -A.length + 1; dy <= A.length -1; dy++) {
                int overlap = 0;

                for (int i = 0; i < A.length; i++) {
                    for (int j = 0; j < A.length; j++ ){
                        if (B[i][j] == 1) {
                            int new_i = i + dx;
                            int new_j = j + dy;

                            if (isValid(new_i, new_j, A.length) && A[new_i][new_j] == 1)
                                overlap += 1;
                        }

                    }
                }

                ret = Math.max(ret, overlap);
            }
        }


        return ret;
    }

    private boolean isValid(int i, int j, int max_len) {
        return i >= 0 && i < max_len && j >= 0 && j < max_len;
    }
}
