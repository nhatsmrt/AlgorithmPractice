class Solution {
    public boolean isMonotonic(int[] A) {
        if (A.length <= 1)
            return true;

        boolean start = false;
        boolean increasing = false;
        for (int i = 1; i < A.length; i++) {
            if (A[i - 1] < A[i]) {
                if (!start) {
                    start = true;
                    increasing = true;
                }
                else if (start && !increasing)
                    return false;
            }
            else if (A[i - 1] > A[i]) {
                if (!start) {
                    start = true;
                    increasing = false;
                }
                else if (start && increasing)
                    return false;
            }
        }

        return true;
    }
}
