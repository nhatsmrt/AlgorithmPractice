class Solution {
    public int[] productExceptSelf(int[] nums) {
        int [] ret = new int[nums.length];

        ret[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            ret[i] = ret[i - 1] * nums[i - 1];
        }

        int R = 1;
        for (int j = nums.length - 2; j >= 0; j--) {
            R *= nums[j + 1];
            ret[j] *= R;
        }
        return ret;
    }
}
