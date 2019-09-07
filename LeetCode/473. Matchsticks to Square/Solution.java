class Solution {
    private int[] dpMap;
    private int[] maskToSumMap;

    public boolean makesquare(int[] nums) {
        if (nums.length == 0)
            return false;

        int perimeter = 0;
        for (int i = 0; i < nums.length; i++)
            perimeter += nums[i];
        if (perimeter % 4 != 0)
            return false;

        int side = perimeter / 4;

        dpMap = new int[1 << (nums.length)];
        maskToSumMap = new int[1 << (nums.length)];
        maskToSumMap[maskToSumMap.length - 1] = perimeter;

        return dp(nums, (1 << (nums.length)) - 1, side);
    }

    private boolean dp(int[] nums, int mask, int side) {

        if (dpMap[mask] != 0)
            return dpMap[mask] == 1;

        if (mask == 0)
            return true;

        int ret = 2;
        if (sumWithMask(nums, mask) == side) {
            ret = 1;
        }
        else {
            for (int i = 1; i < mask; i++) {
                if ((i & mask) == i) {
                    if (sumWithMask(nums, i) % side == 0) {
                        if (dp(nums, i, side) && dp(nums, mask - i, side)) {
                            ret = 1;
                            break;
                        }
                    }
                }
            }
        }
        dpMap[mask] = ret;
        return ret == 1;

    }


    public int sumWithMask(int[] nums, int mask) {
        if (mask == 0)
            return 0;

        if (maskToSumMap[mask] != 0)
            return maskToSumMap[mask];

        int sum = 0;
        int i = 0;

        while (1 << i <= mask) {
            if(((1 << i) & mask) > 0) {
                sum = nums[i] + sumWithMask(nums, mask - (1 << i));
                break;
            }
            i += 1;
        }
        maskToSumMap[mask] = sum;
        return sum;
    }
}
