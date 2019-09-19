class Solution {
    public int reversePairs(int[] nums) {
        int ret = 0;
        List<Integer> list = new ArrayList<Integer>();

        for (int i = nums.length - 1; i >= 0; i--) {
            int half = div2(nums[i]);
            int insertionPoint = Collections.binarySearch(list, half);
            if (insertionPoint < 0)
                insertionPoint = -insertionPoint - 1;
            else {
                while (insertionPoint > 0 && list.get(insertionPoint - 1) == half)
                    insertionPoint -= 1;
            }

            ret += insertionPoint;

            insertionPoint = Collections.binarySearch(list, nums[i]);
            if (insertionPoint < 0)
                insertionPoint = -insertionPoint - 1;
            if (insertionPoint < list.size())
                list.add(insertionPoint, nums[i]);
            else
                list.add(nums[i]);
        }
        return ret;
    }

    private int div2(int num) {
        if (num % 2 == 0 || num < 0)
            return num / 2;
        else
            return num / 2 + 1;
    }
}
