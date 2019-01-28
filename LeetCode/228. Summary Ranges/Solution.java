class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ret = new ArrayList<String>();
        int start = 0;
        int end = 0;

        while (start < nums.length) {
            end = start;
            while (end < nums.length && nums[end] - nums[start] == end - start)
                end += 1;

            end -= 1;

            String summary;
            if (start != end)
                summary = nums[start] + "->" + nums[end];
            else
                summary = "" + nums[start];

            ret.add(summary);
            start = end + 1;
        }

        return ret;
    }


}
