class Solution2 {
    public int monotoneIncreasingDigits(int N) {
        if (N < 10)
            return N;

        int scale = 1;
        int numDig = 1;
        while (scale * 10 <= N) {
            scale *= 10;
            numDig += 1;
        }

        int[] Ndigs = new int[numDig];
        for (int i = 0; i < Ndigs.length; i++) {
            Ndigs[i] = N / scale;
            N %= scale;
            scale /= 10;
        }

        int ret = 0;
        int peak = 0;
        while (peak < numDig - 1 && Ndigs[peak] <= Ndigs[peak + 1]) {
            peak += 1;
        }

        while (peak > 0 && Ndigs[peak] == Ndigs[peak - 1])
            peak -= 1;

        for (int i = 0; i < peak; i++)
            ret = ret * 10 + Ndigs[i];

        if (peak == numDig - 1)
            ret = ret * 10 + Ndigs[peak];
        else {
            ret = ret * 10 + Ndigs[peak] - 1;
            for (int i = peak + 1; i < numDig; i++)
                ret = ret * 10 + 9;
        }

        return ret;
    }
}
