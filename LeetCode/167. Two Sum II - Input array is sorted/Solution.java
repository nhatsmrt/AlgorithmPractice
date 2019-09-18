class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] ret = new int[2];
        int start = 0;
        int end = numbers.length - 1;

        while (start < end) {
            int sum = numbers[start] + numbers[end];
            if (sum == target) {
                ret[0] = start + 1;
                ret[1] = end + 1;
                break;
            }
            else if (sum > target) {
                end = Arrays.binarySearch(numbers, start + 1, end - 1, target - numbers[start]);
                if (end < 0)
                    end = -end - 1;
            }
            else {
                start = Arrays.binarySearch(numbers, start + 1, end, target - numbers[end]);
                if (start < 0)
                    start = -start - 1;
            }
        }

        return ret;
    }
}
