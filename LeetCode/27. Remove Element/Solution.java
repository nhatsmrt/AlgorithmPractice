class Solution {
    public int removeElement(int[] nums, int val) {
        int finalLength = nums.length;
        int i = 0;

        while (i < nums.length && i < finalLength) {
            if (nums[i] == val) {
                for (int j = i + 1;j < finalLength; j++)
                    nums[j - 1] = nums[j];
                finalLength -= 1;
            }
            else
                i += 1;
        }

        return finalLength;
    }
}
