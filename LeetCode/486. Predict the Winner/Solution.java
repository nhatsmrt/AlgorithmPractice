class Solution {
    int[][][] scores;
    public int findMaxScoreDP(int[] nums, int i, int j, int player) {
        if (scores[i][j][player] != -1)
            return scores[i][j][player];

        int chooseFirst = nums[i] + findMaxScoreDP(nums, i + 1, j, 1);
        int chooseLast = nums[j] + findMaxScoreDP(nums, i, j - 1, 1);
        int ret = 0;

        if (player == 0)
            ret = chooseFirst > chooseLast ? chooseFirst : chooseLast;
        else {
            if (chooseFirst >= chooseLast)
                ret = findMaxScoreDP(nums, i + 1, j, 0);
            else
                ret = findMaxScoreDP(nums, i, j - 1, 0);
        }


        scores[i][j][player] = ret;

        return ret;
    }
    public boolean PredictTheWinner(int[] nums) {
        int size = nums.length;
        if (size <= 2)
            return true;

        scores = new int[size][size][2];
        for (int[][] starts : scores) {
            for (int[] ends : starts)
                Arrays.fill(ends, -1);
        }

        for (int i = 0; i < size; i++) {
            scores[i][i][0] = nums[i];
            scores[i][i][1] = 0;

            if (i < size - 1) {
                scores[i][i + 1][0] = nums[i] > nums[i + 1] ? nums[i] : nums[i + 1];
                scores[i][i + 1][1] = nums[i] > nums[i + 1] ? nums[i + 1] : nums[i];
            }

        }

        int totalSum = 0;
        for (int i = 0; i < size; i++)
            totalSum += nums[i];

        int firstPlayerScore = findMaxScoreDP(nums, 0, size - 1, 0);
        int secondPlayerScore = totalSum - firstPlayerScore;

        return firstPlayerScore >= secondPlayerScore;
    }
}
