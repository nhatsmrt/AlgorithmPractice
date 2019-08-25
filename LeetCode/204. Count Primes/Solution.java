class Solution {
    public int countPrimes(int n) {
        int ret = 0;
        int[] sieve = new int[n + 1];

        for (int i = 2; i < n; i++) {
            if (sieve[i] == 0) {
                ret += 1;
                for (int j = 1; j <= n / i; j++)
                    sieve[i * j] = -1;
            }
        }
        
        return ret;
    }
}
