class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1)
            return s;

        StringBuilder ret = new StringBuilder();
        int bigStepSize = 2 * numRows - 2;

        for (int i = 0; i < numRows; i++) {
            if (i < s.length()) {
                ret.append(s.charAt(i));

                int move = bigStepSize - 2 * i;
                int it = i + move;
                while (it < s.length()) {
                    if (move != 0)
                        ret.append(s.charAt(it));
                    move = bigStepSize - move;
                    it += move;
                }
            }
        }
        return ret.toString();
    }
}
