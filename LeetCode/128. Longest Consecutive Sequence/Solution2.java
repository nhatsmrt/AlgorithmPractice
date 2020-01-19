class Solution2 {
    public int longestConsecutive(int[] nums) {
        // O(n) time and space complexity
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums)
            numSet.add(num);

        int ret = 0;
        for (int num : nums) {
            if (!numSet.contains(num - 1)) {
                int end = num + 1;

                while (numSet.contains(end))
                    end += 1;

                int candidate = end - num;
                if (candidate > ret)
                    ret = candidate;
            }
        }

        return ret;
    }
}
