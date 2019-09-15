class Solution {
    public double myPow(double x, int n) {
        if ((x < 1.0 && x > -1.0 && n > 1000000) || (x > 1.0 || x < -1.0) && (n < -1000000))
            return 0.0;

        if (x == 0)
            return 0;

        if (x == 1 || n == 0)
            return 1.0;

        if (x == -1) {
            if (n % 2 == 0)
                return 1.0;
            else
                return -1.0;
        }

        if (n < 0)
            return 1 / myPow(x, - n);


        double ret = 1.0;
        int pow = 1;
        double powers = x;
        while (pow <= n) {
            if (pow > 1)
                powers = powers * powers;

            if ((n & pow) > 0)
                ret = ret * powers;

            pow *= 2;
        }

        return ret;
    }
}
