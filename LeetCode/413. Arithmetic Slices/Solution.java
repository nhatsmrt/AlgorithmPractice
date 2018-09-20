class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        int size = A.length;

        if (size < 3)
            return 0;

        int[] furthest = new int[size];
        int ret = 0;
        int oldVal = 0;

        for (int i = 0; i < size - 2; i++) {
            oldVal = i > 0 ? furthest[i] : 2;

            if (oldVal >= i + 2)
                furthest[i] = oldVal;
            else
                furthest[i] = i + 2;

            while(furthest[i] < size && A[i + 1] - A[i] == A[furthest[i]] - A[furthest[i] - 1])
                furthest[i] += 1;

            if (furthest[i] > oldVal) {
                furthest[i] -= 1;
                ret += (furthest[i] - i - 1);
            }
        }

        return ret;
    }
}
