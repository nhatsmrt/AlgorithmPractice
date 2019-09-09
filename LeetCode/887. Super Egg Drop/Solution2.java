class Solution2 {

    public int superEggDrop(int K, int N) {
        int left = 1;
        int right = N;

        while (left < right) {
            int mid = (right + left) / 2;
            if (binomSum(mid, K, N) < N)
                left = mid + 1;
            else
                right = mid;
        }

        return left;
    }


    private int binomSum(int T, int K, int N) {
        int ret = 0;
        int binom = 1; // = binom{T}{0}
        for (int i = 0; i < K; i++) {
            binom *= (T - i);
            binom /= (i + 1); // = binom{T}{i + 1}, from i = 0 to K - 1
            ret += binom;
            if (ret > N)
                break; // truncate computation to prevent overflow and speed up
        }
        return ret;
    }
}
