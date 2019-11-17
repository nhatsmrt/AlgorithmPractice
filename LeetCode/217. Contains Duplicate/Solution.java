class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numSet = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++)
            numSet.add(nums[i]);
        return numSet.size() != nums.length;
    }
}
