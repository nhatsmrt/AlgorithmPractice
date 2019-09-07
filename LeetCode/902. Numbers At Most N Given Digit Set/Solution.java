class Solution {
    private int[] dp;

    public int atMostNGivenDigitSet(String[] D, int N) {
        int numDig = 1;
        int scale = 1;

        int[] Dint = new int[D.length];
        for (int i = 0; i < D.length; i++)
            Dint[i] = (int) (D[i].charAt(0) - '0');

        while (scale * 10 <= N) {
            scale *= 10;
            numDig += 1;
        }
        int numDigOriginal = numDig;
        int[] NDig = new int[numDig];
        for (int i = 0; i < numDig; i++) {
            NDig[i] = N / scale;
            N %= scale;
            scale /= 10;
        }


        dp = new int[numDig];
        Arrays.fill(dp, -1);
        int ret = atMostNGivenDigitSet(Dint, NDig, 0);
        for (int i = 1; i < numDig; i++)
            ret += (int) Math.pow(D.length, i);
        return ret;
    }

    private int atMostNGivenDigitSet(int[] D, int[] N, int pos) {
        if (dp[pos] != -1)
            return dp[pos];

        int ret = 0;
        int nLessThan = 0;
        int nEqual = 0;

        for (int i = 0; i < D.length; i++) {
            if (D[i] < N[pos])
                nLessThan += 1;
            else if (D[i] == N[pos])
                nEqual += 1;
        }

        if (pos == N.length - 1)
            ret = nLessThan + nEqual;
        else
            ret = nEqual * atMostNGivenDigitSet(D, N, pos + 1) + nLessThan * (int) (Math.pow(D.length, N.length - 1 - pos));

        dp[pos] = ret;
        return ret;
    }
}
