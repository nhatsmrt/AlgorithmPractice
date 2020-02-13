class Solution {
    public int consecutiveNumbersSum(int N) {
        // Time: O(sqrt(N)); Space: O(1)
        int ret = 0;
        int product = 2 * N;
        int upperBound = (int) Math.sqrt(product);

        for (int i = 1; i <= upperBound; i++) {
            if (product % i == 0) {
                int y = product / i + 1 - i;
                if (y > 1 && y % 2 == 0)
                    ret += 1;
            }
        }

        return ret;
    }
}
