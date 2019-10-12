class Solution {
    public List<Integer> pancakeSort(int[] A) {
        List<Integer> ret = new ArrayList<Integer>();
        sort(A, ret, A.length - 1);
        return ret;
    }

    private void sort(int[] A, List<Integer> ret, int end) {
        if (end > 0) {
            int curMax = A[0];
            int maxInd = 0;

            for (int i = 1; i <= end; i++) {
                if (curMax < A[i]) {
                    curMax = A[i];
                    maxInd = i;
                }
            }

            if (maxInd == end)
                sort(A, ret, end - 1);
            else {
                ret.add(maxInd + 1);
                flip(A, maxInd);
                ret.add(end + 1);
                flip(A, end);
                sort(A, ret, end - 1);
            }
        }
    }

    private void flip(int[] A, int end) {
        for (int i = 0; i <= end / 2; i++) {
            int tmp = A[i];
            A[i] = A[end - i];
            A[end - i] = tmp;
        }
    }
}
