class Solution {
    public boolean isPowerOfFour(int num) {
        if (num <= 0)
            return false;

        if (num == 1)
            return true;

        boolean isPower2 = (num & (num - 1)) == 0;
        int numBinDig = 0;
        while (num > 0) {
            numBinDig += 1;
            num = num >> 1;
        }

        return isPower2 && numBinDig % 2 == 1;
    }
}
