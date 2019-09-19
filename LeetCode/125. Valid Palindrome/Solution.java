class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        while (i <= j) {
            char left = s.charAt(i);
            char right = s.charAt(j);


            if (left >= 'a')
                left -= 'a' - 'A';

            if (right >= 'a')
                right -= 'a' - 'A';

            if (isAlphanumeric(left) && isAlphanumeric(right)) {
                if (left != right)
                    return false;
                i += 1;
                j -= 1;
            }
            else {
                if (!isAlphanumeric(left))
                    i += 1;
                if (!isAlphanumeric(right))
                    j -= 1;
            }
        }

        return true;
    }

    private boolean isAlphanumeric(char c) {
        return ('0' <= c && c <= '9') || ('A' <= c && c <= 'Z');
    }
}
