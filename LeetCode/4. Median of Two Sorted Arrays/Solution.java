class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length)
            return findMedianSortedArrays(nums2, nums1);

        return findMedianSortedArrays(
            nums1, nums2,
            0, nums1.length
        );
    }


    private double findMedianSortedArrays(
        int[] nums1, int[] nums2,
        int min, int max
    ) {
        int mid1 = (min + max) / 2;
        int mid2 = (nums1.length + nums2.length + 1) / 2 - mid1;

        if (
            (mid2 == 0 || mid1 == nums1.length || nums2[mid2 - 1] <= nums1[mid1]) &&
            (mid1 == 0 || mid2 == nums2.length || nums1[mid1 - 1] <= nums2[mid2])
           ) {
            if ((nums1.length + nums2.length) % 2 == 1) {
                if (mid2 > 0 && mid1 > 0)
                    return max(nums1[mid1 - 1], nums2[mid2 - 1]);
                else if (mid2 > 0)
                    return nums2[mid2 - 1];
                else
                    return nums1[mid1 - 1];
            }
            else {
                double lower, upper;
                if (mid2 > 0 && mid1 > 0)
                    lower = max(nums1[mid1 - 1], nums2[mid2 - 1]);
                else if (mid2 > 0)
                    lower = nums2[mid2 - 1];
                else
                    lower = nums1[mid1 - 1];


                if (mid2 < nums2.length && mid1 < nums1.length)
                    upper =  min(nums1[mid1], nums2[mid2]);
                else if (mid2 < nums2.length)
                    upper = nums2[mid2];
                else
                    upper = nums1[mid1];

                return ((double) lower + upper) / 2;

            }
        }
        else if (mid2 > 0 && mid1 < nums1.length && nums2[mid2 - 1] > nums1[mid1])
            return findMedianSortedArrays(nums1, nums2, mid1 + 1, max);
        else
            return findMedianSortedArrays(nums1, nums2, min, mid1 - 1);


    }

    private double min(int a, int b) {
        return a < b ? a : b;
    }

    private double max(int a, int b) {
        return a > b ? a : b;
    }
}
