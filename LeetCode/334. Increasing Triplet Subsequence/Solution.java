class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums.length < 3)
            return false;

        int i = 0;
        int j = 1;
        int k = 1;
        boolean foundSecond = false;
        while (i < nums.length && j < nums.length) {
            if (!foundSecond) {
                if (nums[i] >= nums[j]) {
                    i = j;
                    j += 1;
                }
                else {
                    foundSecond = true;
                    k = j + 1;
                }
            }
            else if (k < nums.length) {
                if (nums[k] > nums[j])
                    return true;
                else if (nums[k] > nums[i]) {
                    j = k;
                    k += 1;
                }
                else {
                    k += 1;
                }
            }
            else {
                i = j + 1;
                j = i + 1;
                foundSecond = false;
            }
        }

        return false;
    }
}
