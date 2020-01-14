class Solution {
    public int trailingZeroes(int n) {
        if (n < 0)
            return trailingZeroes(-n);

        return vp(n, 5);
    }

    private int vp(int n, int p) {
        // p must be prime
        // v_p(n) = highest power k such that p^k | n
        // Legendre's theorem:
        // v_p(n) = \sum_{k: p^k <= n} floor(n / p^k)
        // Complexity: O(log_p(n))

        int ret = 0;

        while (n > 0) {
            n /= p;
            ret += n;
        }

        return ret;
    }
}
