class Solution {
    int[] uglyNumber = new int[1691];

    public int min(int a, int b, int c) {
        if (a <= b && a <= c)
            return a;
        else if (b <= a && b <= c)
            return b;

        return c;
    }

    public int max(int a, int b) {
        return a > b ? a : b;
    }


    public int nthUglyNumber(int n) {
        uglyNumber[1] = 1;
        uglyNumber[2] = 2;
        uglyNumber[3] = 3;
        uglyNumber[4] = 4;


        if (uglyNumber[n] != 0)
            return uglyNumber[n];

        int curMin = 2147483647;
        for (int i = 1; i <= n - 1; i++) {
            if (nthUglyNumber(i) > nthUglyNumber(n - 1) / 5 && nthUglyNumber(i) <= 2147483647 / 2) {
                if (
                    nthUglyNumber(i) <= 2147483647 / 2 &&
                    nthUglyNumber(i) * 2 > nthUglyNumber(n - 1) &&
                    nthUglyNumber(i) * 2 < curMin
                )
                    curMin = nthUglyNumber(i) * 2;
                else if (
                    nthUglyNumber(i) <= 2147483647 / 3 &&
                    nthUglyNumber(i) * 3 > nthUglyNumber(n - 1) &&
                    nthUglyNumber(i) * 3 < curMin
                )
                    curMin = nthUglyNumber(i) * 3;
                else if (
                    nthUglyNumber(i) <= 2147483647 / 5 &&
                    nthUglyNumber(i) * 5 > nthUglyNumber(n - 1) &&
                    nthUglyNumber(i) * 5 < curMin
                )
                    curMin = nthUglyNumber(i) * 5;
            }
        }

        uglyNumber[n] = curMin;
        return curMin;

    }
}
