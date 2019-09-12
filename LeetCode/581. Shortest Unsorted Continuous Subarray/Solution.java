class Solution {
    public int findUnsortedSubarray(int[] nums) {
        Stack<Integer> stack = new Stack<Integer>();
        int upperBound = nums.length - 1;
        while (upperBound >= 0 && (stack.isEmpty() || stack.peek() >= nums[upperBound])) {
            stack.push(nums[upperBound]);
            upperBound -= 1;
        }
        upperBound += 1;
        for (int i = upperBound - 1; i >= 0; i--) {
            while(!stack.isEmpty() && stack.peek() < nums[i]) {
                upperBound += 1;
                stack.pop();
            }
            if (stack.isEmpty())
                break;
        }

        stack = new Stack<Integer>();
        int lowerBound = 0;
        while (lowerBound < nums.length && (stack.isEmpty() || stack.peek() <= nums[lowerBound])) {
            stack.push(nums[lowerBound]);
            lowerBound += 1;
        }
        lowerBound -= 1;

        for (int i = lowerBound + 1; i < nums.length; i++) {
            while(!stack.isEmpty() && stack.peek() > nums[i]){
                lowerBound -= 1;
                stack.pop();
            }
            if (stack.isEmpty())
                break;
        }

        if (upperBound <= lowerBound)
            return 0;

        return upperBound - lowerBound - 1;
    }
}
