class Solution {
    private int[][] dp;
    private SparseTable st;

    public int minDifficulty(int[] jobDifficulty, int d) {
        // dp[i][j] is the difficulty of painting first i + 1 boards using j + 1 days
        // dp[i][j] = min_{k = j - 1}^{i - 1} dp[k][j - 1] + max(A[k + 1:i + 1])
        // Time complexity: O(n^3d)
        // Using segment tree for range max query reduce time complexity to O(n^2 log n d)
        // Using sparse table for range max query reduce time complexity to O(n^2 d)

        if (jobDifficulty.length < d)
            return -1;

        st = new SparseTable(jobDifficulty);
        dp = new int[jobDifficulty.length][d];
        for (int[] subarr : dp)
            Arrays.fill(subarr, -1);
        return minDifficulty(jobDifficulty.length - 1, d - 1);

    }

    private int minDifficulty(int i, int j) {
        if (i == -1 || j == -1)
            return i == - 1 && j == -1 ? 0 : -1;

        if (i < j)
            return -1;

        if (dp[i][j] != -1)
            return dp[i][j];

        int ret = -1;
        for (int k = j - 1; k < i; k++) {
            int candidate = minDifficulty(k, j - 1);
            if (candidate != -1) {
                candidate += st.query(k + 1, i);
                if (ret == -1 || candidate < ret)
                    ret = candidate;
            }
        }

        dp[i][j] = ret;
        return ret;


    }

    private class SparseTable {
        private int[][] data;
        // data[i][j] = max(arr[j:j + (1 << i)])

        public SparseTable(int[] arr) {
            int numRow = log2(arr.length) + 1;
            data = new int[numRow][arr.length];

            for (int j = 0; j < arr.length; j++) {
                data[0][j] = arr[j];
            }

            // data[i][j] = max(data[i - 1][j], data[i - 1][j + (1 << (i - 1))])
            for (int i = 1; i < numRow; i++) {
                for (int j = 0; j < arr.length - (1 << i) + 1; j++) {
                    data[i][j] = Math.max(data[i - 1][j], data[i - 1][j + (1 << (i - 1))]);
                }
            }

        }

        public int query(int low, int high) {
            int row = log2(high - low + 1);
            return Math.max(data[row][low], data[row][high - (1 << row) + 1]);
        }

        private int log2(int num) {
            return (int) (Math.log(num) / Math.log(2) + 1e-10);
        }
    }

}
