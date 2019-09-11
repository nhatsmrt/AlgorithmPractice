class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 1)
            return 1;

        int it = 1;
        int curInd = 0;

        while (it < nums.length) {
            if (nums[it] != nums[curInd]) {
                curInd += 1;
                nums[curInd] = nums[it];
            }
            it += 1;
        }

        return curInd + 1;
    }
}
