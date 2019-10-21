class Solution2 {

    public int splitArray(int[] nums, int m) {
        // LC's official Sol
        // Complexity: O(n log (sum(nums)))
        long left = 0;
        long right = 0;
        for (int i = 0; i < nums.length; i++) {
            right += nums[i];
            if (left <= nums[i])
                left = nums[i];
        }

        long ans = right;
        while (left <= right) {
            long mid = (left + right) >> 1;
            int sum = 0;
            int cnt = 1;
            for (int i = 0; i < nums.length; i++) {
                if (sum + nums[i] > mid) {
                    cnt += 1;
                    sum = nums[i];
                }
                else
                    sum += nums[i];
            }

            if (cnt <= m) {
                ans = Math.min(ans, mid);
                right = mid - 1;
            }
            else
                left = mid + 1;
        }

        return (int) ans;

    }
}
