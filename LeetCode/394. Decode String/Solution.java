class Solution {
    public String decodeString(String s) {
        return recursiveDecode(s, 0, s.length() - 1).toString();
    }

    private StringBuilder recursiveDecode(String s, int start, int end) {
        StringBuilder ret = new StringBuilder();
        int i = start;
        int numRep = 0;

        while (i <= end) {
            if (isChar(s.charAt(i)))
                ret.append(s.charAt(i));
            else if (isDigit(s.charAt(i)))
                numRep = 10 * numRep + (int) (s.charAt(i) - '0');
            else {
                int numOpen = 1;
                int j = i + 1;
                while (numOpen != 0) {
                    if (s.charAt(j) == ']')
                        numOpen -= 1;
                    else if (s.charAt(j) == '[')
                        numOpen += 1;
                    j += 1;
                }

                j -= 1; // now j is at ]
                StringBuilder inner = recursiveDecode(s, i + 1, j - 1);
                for (int r = 0; r < numRep; r++)
                    ret.append(inner);

                i = j;
                numRep = 0;
            }
            i += 1;
        }
        return ret;
    }

    private boolean isDigit(char c) {
        return '0' <= c && c <= '9';
    }

    private boolean isChar(char c) {
        return !isDigit(c) && c != '[' && c != ']';
    }
}
