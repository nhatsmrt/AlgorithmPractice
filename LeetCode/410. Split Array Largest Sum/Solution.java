class Solution {
    private int[][] dp;
    private int[] prefix;

    public int splitArray(int[] nums, int m) {
        dp = new int[nums.length][m];

        prefix = new int[nums.length + 1];
        prefix[0] = 0;

        for (int i = 0; i < nums.length; i++) {
            Arrays.fill(dp[i], -1);
            prefix[i + 1] = prefix[i] + nums[i];
        }

        // dp[pos][remaining] = min_j(max(cost[pos][j], dp[j][remaining - 1]))
        // note that cost[pos][j] is monotonically increasing in j
        // dp[j][remaining - 1] is a monotonically decreasing in j
        // so optimal j is at one of the 2 points where these two values are closest
        // j can be found by modified binary search
        // complexity: O(mn log n)
        return splitArray(nums, 0, m - 1);
    }

    private int splitArray(int[] nums, int pos, int remaining) {
        if (dp[pos][remaining] != -1)
            return dp[pos][remaining];

        int ret = -1;
        if (remaining == nums.length - 1 - pos) {
            for (int i = pos; i < nums.length; i++) {
                if (ret < nums[i])
                    ret = nums[i];
            }
        }
        else if (remaining == 0)
            ret = sum(nums, pos, nums.length - 1);
        else
            ret = search(nums, pos, nums.length - 1 - remaining, remaining);

        dp[pos][remaining] = ret;
        return ret;
    }

    private int sum(int[] nums, int from, int to) {
        int ret = 0;
        for (int i = from; i <= to; i++) {
            ret += nums[i];
        }

        return ret;
    }

    private int search(int[] nums, int from, int to, int remaining) {
        int ret = 0;
        int left = from;
        int right = to;

        while (right > left + 1) {
            int mid  = (right + left) >> 1;
            int first = prefix[mid + 1] - prefix[from];
            int second = splitArray(nums, mid + 1, remaining - 1);
            if (first == second)
                return first;
            else if (first > second)
                right = mid;
            else
                left = mid;
        }


        if (right == left) {
            int first = prefix[left + 1] - prefix[from];
            int second = splitArray(nums, left + 1, remaining - 1);
            return Math.max(first, second);
        }
        else {
            // right = left + 1
            int first = prefix[left + 1] - prefix[from];
            int second = splitArray(nums, left + 1, remaining - 1);
            int candidate1 = Math.max(first, second);
            first = prefix[right + 1] - prefix[from];
            second = splitArray(nums, right + 1, remaining - 1);
            int candidate2 = Math.max(first, second);
            return Math.min(candidate1, candidate2);
        }
    }
}
