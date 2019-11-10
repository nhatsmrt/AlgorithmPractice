class Solution {

    public String minWindow(String S, String T) {
        // time complexity: O(mn)
        int start = 0;
        int end = -1;
        int it = 0;
        int retStart = -1;
        int retEnd = -1;

        while (start < S.length() && end < S.length()) {
            for (it = 0; it < T.length(); it++) {
                end += 1;
                while (end < S.length() && S.charAt(end) != T.charAt(it))
                    end += 1;
            }

            if (it == T.length() && end < S.length()) {
                start = end;
                for (it = T.length() - 2; it >= 0; it--) {
                    start -= 1;
                    while (S.charAt(start) != T.charAt(it))
                        start -= 1;
                }
                if (retEnd == -1 || end - start + 1 < retEnd - retStart + 1) {
                    retEnd = end;
                    retStart = start;
                }
                end = start + 1;
            }
        }

        if (retEnd >= 0)
            return S.substring(retStart, retEnd + 1);
        return "";
    }

}
