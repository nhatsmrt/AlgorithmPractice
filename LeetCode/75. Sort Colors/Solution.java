class Solution {
// Solution 1: Counting Sort
//     public void sortColors(int[] nums) {
//         int num0 = 0;
//         int num1 = 0;
//         int num2 = 0;

//         for (int num : nums) {
//             if (num == 0)
//                 num0 += 1;
//             else if (num == 1)
//                 num1 += 1;

//             num2 += 1;
//         }
//         // System.out.println(num0);

//         for (int i = 0; i < nums.length; i++) {
//             if (i < num0)
//                 nums[i] = 0;
//             else if (i < num0 + num1)
//                 nums[i] = 1;
//             else
//                 nums[i] = 2;
//         }
//     }

    public void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    public void sortColors(int[] nums) {
        int num0 = 0;
        int num1 = 0;
        int num2 = 0;

        for (int i = 0; i < nums.length; i++) {
            if(nums[i] == 0) {
                swap(nums, i, num0);
                num0 += 1;

                if (nums[i] == 1)
                    swap(nums, i, num0 + num1 - 1);
            }
            else if(nums[i] == 1) {
                swap(nums, i, num0 + num1);
                num1 += 1;
            }
        }
    }
}
