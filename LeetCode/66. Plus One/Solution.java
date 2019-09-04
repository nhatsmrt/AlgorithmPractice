class Solution {
    public int[] plusOne(int[] digits) {
        return plusOne(digits, digits.length - 1);
    }

    private int[] plusOne(int[] digits, int ind) {
        if (ind == -1) {
            int[] ret = new int[digits.length + 1];
            ret[0] = 1;
            for (int i = 0; i < digits.length; i++)
                ret[i + 1] = digits[i];
            return ret;
        }
        else {
            if (digits[ind] < 9) {
                digits[ind] += 1;
                return digits;
            }
            else {
                digits[ind] = 0;
                return plusOne(digits, ind - 1);
            }
        }
    }
}
