class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashTable = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            hashTable.put(nums[i], i);
        }

        int[] ret = new int[2];
        for (int i = 0; i < nums.length; i++) {
            if (hashTable.containsKey(target - nums[i]) && hashTable.get(target - nums[i]) != i) {
                ret[0] = i;
                ret[1] = hashTable.get(target - nums[i]);
                break;
            }
        }
        return ret;
    }
}
