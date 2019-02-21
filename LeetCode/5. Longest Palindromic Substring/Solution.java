// implement Manacher's algorithm
// based on https://www.hackerearth.com/practice/algorithms/string-algorithm/manachars-algorithm/tutorial/
class Solution {

    // transform original string to include special characters
    private String expandString(String s) {
        String ret = "$";
        int strLen = s.length();

        for (int i = 0; i < strLen; i++)
            ret += "#" + s.charAt(i);

        ret += "#@";

        return ret;
    }

    public String longestPalindrome(String s) {
        String expanded = expandString(s);

        // current center and right limit
        int center = 0;
        int right = 0;

        int[] P = new int[2 * s.length() + 3]; // palindrome array of expanded s
        // P[i] = 1/2 longest palindrome substring centered at i

        // compute P
        for (int i = 1; i < expanded.length() - 1; i++) {
            int iMirror = center - (i - center); // corresponding letter in palindrome substring

            // if i falls withing the range of longest palindrome center at c
            // mirror property applies
            if (right > i)
                P[i] = min(right - i, P[iMirror]);

            // Expanding around center i:
            while (expanded.charAt(i + 1 + P[i]) == expanded.charAt(i - 1 - P[i]))
                P[i] += 1;

            // Update c, r if the palindrome expands past r:
            if (i + P[i] > right) {
                center = i;
                right = i + P[i];
            }
        }


        int maxPalindromeSize = 0;
        int centerIndex = 0;

        for (int i = 2; i < expanded.length(); i++) {
            if (P[i] > maxPalindromeSize) {
                maxPalindromeSize = P[i];
                centerIndex = i;
            }
        }


        return s.substring(
            (centerIndex - 1 - maxPalindromeSize) / 2,
            (centerIndex - 1 - maxPalindromeSize) / 2 + maxPalindromeSize
        );
    }


    private int min(int a, int b) {
        return a < b ? a : b;
    }
}
