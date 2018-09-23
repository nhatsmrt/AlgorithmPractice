class Solution {
    public int[] tilings;
    public int numTilingsDP(int N) {
        if (tilings[N] != -1)
            return tilings[N];

        int ret = 0;
        ret += numTilingsDP(N - 1) + numTilingsDP(N - 2);
        ret = ret  % 1000000007;

        for (int i = 3; i <= N; i++) {
            int incr = 2 * numTilingsDP(N - i) % 1000000007;
            ret += incr;
            ret = ret  % 1000000007;
        }

        tilings[N] = ret;
        return ret;
    }
    public int numTilings(int N) {
        tilings = new int[N + 1];
        Arrays.fill(tilings, - 1);
        tilings[0] = tilings [1] = 1;

        return numTilingsDP(N);
    }
}
