class Solution {
    public boolean find132pattern(int[] nums) {
        if (nums.length < 3)
            return false;

        int[] min = new int[nums.length];
        int[] max = new int[nums.length];

        Deque<Integer> deque = new LinkedList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            while (!deque.isEmpty() && nums[deque.peekLast()] > nums[i])
                deque.removeLast();

            if (deque.isEmpty())
                min[i] = i;
            else
                min[i] = deque.peekFirst();

            deque.addLast(i);
        }

        deque = new LinkedList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i])
                deque.removeLast();

            if (deque.isEmpty())
                max[i] = i;
            else
                max[i] = deque.peekLast();
            deque.addLast(i);
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[max[i]] != nums[i] && nums[min[max[i]]] != nums[max[i]] && nums[i] > nums[min[max[i]]])
                return true;
        }

        return false;
    }
}
