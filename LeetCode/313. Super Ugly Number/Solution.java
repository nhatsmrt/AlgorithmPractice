class Solution {
    int[] dp;

    public int nthSuperUglyNumber(int n, int[] primes) {
        // Time Complexity: O(nklog n)
        // Space Complexity: O(n)

        dp = new int[n];
        dp[0] = 1;

        for (int i = 1; i < n; i++)
            nthSuperUglyNumberDP(i, primes);
        return nthSuperUglyNumberDP(n - 1, primes);
    }

    private int nthSuperUglyNumberDP(int n, int[] primes) {
        if (dp[n] != 0)
            return dp[n];

        long ret = (long) (nthSuperUglyNumberDP(n - 1, primes)) * primes[0];
        int ind = n - 1;
        for (int i = 0; i < primes.length; i++) {
            int ratio = nthSuperUglyNumberDP(n - 1, primes) / primes[i];
            ind = Arrays.binarySearch(dp, 0, ind + 1, ratio);
            if (ind < 0)
                ind = -ind - 1;
            else
                ind += 1;

            if (ind < n - 1 && checkOverflowProd(dp[ind], primes[i])) {
                int candidate = dp[ind] * primes[i];
                if (candidate < ret && candidate > nthSuperUglyNumberDP(n - 1, primes))
                    ret = candidate;
            }
        }

        dp[n] = (int) ret;
        return (int) ret;
    }

    private boolean checkOverflowProd(int a, int b) {
        return ((a * b) / a) == b;
    }
}
