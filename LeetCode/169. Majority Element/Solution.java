class Solution {
    public int majorityElement(int[] nums) {
        int curMajor = 0;
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            if (counter == 0) {
                curMajor = nums[i];
                counter = 1;
            }
            else if (curMajor == nums[i])
                counter += 1;
            else
                counter -= 1;
        }
        return curMajor;
    }
}
