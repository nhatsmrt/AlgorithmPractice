class Solution {
    private Map<Integer, Integer> factorial;

    public int numPrimeArrangements(int n) {
        factorial = new HashMap<Integer, Integer>();
        factorial.put(0, 1);
        factorial.put(1, 1);
        factorial.put(2, 2);

        int numPrime = numPrime(n);
        long retLong = ((long) factorial(numPrime) * factorial(n - numPrime)) % 1000000007;
        return (int) retLong;
    }

    private int numPrime(int n) {
        if (n <= 1)
            return 0;
        if (n == 2)
            return 1;

        int[] isPrime = new int[n + 1];
        // Arrays.fill(isPrime, -1);
        int ret = 0;
        for (int i = 2; i <= n; i++) {
            if (isPrime[i] == 0) {
                ret += 1;
                for (int j = 1; i * j <= n; j++)
                    isPrime[i * j] = -1;
            }
        }

        return ret;
    }

    private int factorial(int n) {
        if (factorial.containsKey(n))
            return factorial.get(n);

        long retLong = ((long) factorial(n - 1) * n) % 1000000007;
        int ret = (int) retLong;
        factorial.put(n, ret);
        return ret;
    }
}
