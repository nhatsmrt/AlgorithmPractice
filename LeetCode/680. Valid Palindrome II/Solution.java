class Solution {
    public boolean validPalindrome(String s) {
        return validPalindrome(s, 0, s.length() - 1, false);
    }

    private boolean validPalindrome(String s, int i, int j, boolean found) {
        if (j - i + 1 <= 1)
            return true;
        if (j - i + 1 == 2) {
            if (!found || s.charAt(i) == s.charAt(j))
                return true;
            return false;
        }

        if (s.charAt(i) != s.charAt(j)) {
            if (found)
                return false;
            else
                return validPalindrome(s, i, j - 1, true) || validPalindrome(s, i + 1, j, true);
        }

        return validPalindrome(s, i + 1, j - 1, found);
    }
}
