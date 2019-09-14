class Solution {
    public int mySqrt(int x) {
        if (x == 0)
            return 0;

        double ret = 1;
        for (int i = 0; i < 20; i++)
            ret = (ret + x / ret) / 2;
        return (int) ret;
    }
}
