class Solution {
    public boolean isHappy(int n) {
        if (n < 10) {
            if (n == 1 || n == 7)
                return true;
            else
                return false;
        }
        return isHappy(transform(n));
    }

    private int transform(int n) {
        int ret = 0;
        while (n > 0) {
            int dig = n % 10;
            n /= 10;
            ret += dig * dig;
        }

        return ret;
    }
}
