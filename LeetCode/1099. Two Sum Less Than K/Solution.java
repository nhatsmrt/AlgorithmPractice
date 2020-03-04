class Solution {
    public int twoSumLessThanK(int[] A, int K) {
        // O(n log(n)); can get down to O(n) if use counting sort
        if (A.length < 2)
            return -1;

        Arrays.sort(A);
        if (A[0] + A[1] >= K)
            return -1;

        int i = 0;
        int j = A.length - 1;

        int ret = -1;
        int candidate = A[i] + A[j];

        while (i < j) {
            if (candidate < K)
                ret = Math.max(ret, candidate);

            if (A[i] + A[j] < K)
                i += 1;
            else
                j -= 1;
            candidate = A[i] + A[j];
        }

        return ret;
    }
}
