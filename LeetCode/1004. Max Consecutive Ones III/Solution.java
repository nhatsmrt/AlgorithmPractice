class Solution {
    public int longestOnes(int[] A, int K) {
        int ret = -1;
        int start = 0;
        int end = -1;
        int changed = 0;

        while (end <= A.length) {
            end += 1;
            if (end == A.length) {
                int candidate = end - start;
                if (candidate > ret || ret == -1)
                    ret = candidate;
            }
            else if (A[end] == 0) {
                if (changed < K)
                    changed += 1;
                else {
                    int candidate = end - start;
                    if (candidate > ret || ret == -1)
                        ret = candidate;

                    while (start < end && A[start] == 1)
                        start += 1;

                    start += 1;
                    if (K > 0)
                }
            }
        }

        return ret;
    }
}
