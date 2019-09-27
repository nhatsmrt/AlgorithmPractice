class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;
        for (int i = 0; i < k; i++)
            sum += nums[i];

        int ind = k;
        double candidate = sum;
        while (ind < nums.length) {
            candidate += nums[ind] - nums[ind - k];
            if (candidate > sum)
                sum = candidate;
            ind += 1;
        }

        return sum / k;
    }
}
