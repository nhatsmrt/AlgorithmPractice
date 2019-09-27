class Solution {
    public int[][] generateMatrix(int n) {
        int[][] ret = new int[n][n];
        for (int i = 0; i < n; i++)
            ret[0][i] = i + 1;

        int dir = 1; // 0: right, 1: down, 2: left, 3: up
        int r = 0;
        int c = n - 1;
        int numFilled = n;
        int stepSize = n - 1;
        int numBigStep = 0;

        while (numFilled < n * n) {
            for (int i = 0; i < stepSize; i++) {
                if (dir == 0)
                    c += 1;
                else if (dir == 1)
                    r += 1;
                else if (dir == 2)
                    c -= 1;
                else if (dir == 3)
                    r -= 1;

                ret[r][c] = numFilled + 1;
                numFilled += 1;
            }

            dir += 1;
            dir %= 4;
            numBigStep += 1;
            if (numBigStep % 2 == 0)
                stepSize -= 1;
        }

        return ret;
    }
}
