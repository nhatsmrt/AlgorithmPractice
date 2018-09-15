class Solution {
    int[] numBits;
    public int countBitsDP(int n) {
        if (numBits[n] != -1)
            return numBits[n];

        numBits[n] = n % 2 + countBitsDP(n / 2);
        return numBits[n];
    }

    public int[] countBits(int num) {

        numBits = new int[num + 1];
        Arrays.fill(numBits, - 1);
        numBits[0] = 0;

        int[] ret = new int[num + 1];
        for (int i = 0; i <= num; i++)
            ret[i] = countBitsDP(i);

        return ret;
    }
}
