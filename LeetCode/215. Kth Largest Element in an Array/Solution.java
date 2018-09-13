class Solution {
    public void swap(int[] nums, int a, int b) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }

    public void heapifyFrom(int[] nums, int ind, int end) {
        int left = 2 * ind + 1;
        int right = 2 * ind + 2;
        int largest;

        if (left < end && nums[left] > nums[ind])
            largest = left;
        else
            largest = ind;
        if (right < end && nums[right] > nums[largest])
            largest = right;

        if(largest != ind) {
            swap(nums, ind, largest);
            heapifyFrom(nums, largest, end);
        }
    }

    public void heapify(int[] nums, int end) {
        for (int i = end / 2 - 1; i >= 0; i--)
            heapifyFrom(nums, i, end);
    }


    public int findKthLargest(int[] nums, int k) {
        int size = nums.length;
        // Heap sort:
        for (int i = 0; i < k; i++) {
            heapify(nums, size - i);
            swap(nums, 0, size - i - 1);
        }

        for (int i = 0; i < size; i++)
            System.out.println(nums[i]);

        return nums[size - k];

    }
}
