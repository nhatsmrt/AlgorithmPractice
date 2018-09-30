class Solution {
    public int gcd(int x, int y) {
        if (x == y)
            return x;

        if (x < y)
            return gcd(y, x);

        if (y == 1)
            return 1;

        if (x % y == 0)
            return y;

        return gcd(y, x % y);

    }

    public boolean canMeasureWater(int x, int y, int z) {
        if (z > x + y)
            return false;

        if (z == x || z == y)
            return true;

        if (x < y)
            return canMeasureWater(y, x, z);

        if (y == 0) {
            if (x == z)
                return true;
            else
                return false;
        }

        int gcd = gcd(x, y);

        return z % gcd == 0;

    }
}
