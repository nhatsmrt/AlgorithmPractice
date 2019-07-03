class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> nums1Set = new HashSet<Integer>();
        Set<Integer> nums2Set = new HashSet<Integer>();
        for (int i = 0; i < nums1.length; i++)
            nums1Set.add(nums1[i]);
        for (int i = 0; i < nums2.length; i++)
            nums2Set.add(nums2[i]);

        nums1Set.retainAll(nums2Set);

        int[] ret = new int[nums1Set.size()];
        int i = 0;
        for (Integer num : nums1Set) {
            ret[i] = num;
            i += 1;
        }

        return ret;
    }
}
