class Solution {
    private List<Integer> squares;
    private int[] numSquaresArr;

    public int numSquares(int n) {
        if (isSquare(n)) {
            return 1;
        }

        numSquaresArr = new int[n + 1];
        squares = new ArrayList<Integer>();
        for (int i = 2; i < n + 1; i++) {
            numSquaresArr[i] = -1;
        }

        for (int i = 1; i < n + 1; i++) {
            numSquaresDP(i);
        }

        return numSquaresArr[n];
    }

    private void numSquaresDP(int n) {
        if (isSquare(n)) {
            squares.add(n);
            numSquaresArr[n] = 1;
        }
        else {
            int curMin = -1;
            for (int i = 0; i < squares.size(); i++) {
                int candidate = numSquaresArr[n - squares.get(i)];
                if (curMin < 0 || curMin > candidate)
                    curMin = candidate;
            }
            numSquaresArr[n] = curMin + 1;
        }
    }

    private boolean isSquare(int n) {
        int sqrt = (int) Math.sqrt(n);
        return sqrt * sqrt == n;
    }
}
