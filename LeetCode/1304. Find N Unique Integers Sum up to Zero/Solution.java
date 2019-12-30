class Solution {
    public int[] sumZero(int n) {
        int[] ret = new int[n];
        int half = n / 2;
        int cnt = 0;

        for (int i = 1; i <= half; i++) {
            ret[cnt] = -i;
            ret[cnt + 1] = i;
            cnt += 2;
        }

        if (n % 2 == 1)
            ret[cnt] = 0;
        return ret;
    }
}
