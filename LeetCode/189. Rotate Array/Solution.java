class Solution {
    public void rotate(int[] nums, int k) {

        int ind = 0;
        int tmp1 = nums[0];
        int tmp2;
        int originalInd = 0;
        int newInd = -1;
        int numChanged = 0;
        int i = 0;

        while (numChanged < nums.length) {
            if (newInd != originalInd) {
                tmp2 = nums[(ind + k) % nums.length];
                nums[(ind + k) % nums.length] = tmp1;

                tmp1 = tmp2;
                ind = (ind + k) % nums.length;
                newInd = ind;
                numChanged += 1;
            }
            else {
                ind = (ind + 1) % nums.length;
                tmp1 = nums[ind];
                originalInd = ind;
            }
        }

    }
}
