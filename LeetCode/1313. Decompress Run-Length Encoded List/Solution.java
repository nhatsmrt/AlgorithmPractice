class Solution {
    public int[] decompressRLElist(int[] nums) {
        int retSize = 0;
        for (int i = 0; i < nums.length; i += 2)
            retSize += nums[i];

        int[] ret = new int[retSize];
        int ind = 0;

        for (int i = 0; i < nums.length; i += 2) {
            for (int j = 0; j < nums[i]; j++) {
                ret[ind] = nums[i + 1];
                ind += 1;
            }
        }

        return ret;
    }
}
