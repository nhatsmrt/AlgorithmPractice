class Solution2 {
    public int scoreOfParentheses(String S) {
        // O(n) time, O(1) space
        int opening = 0;
        int ret = 0;

        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == '(')
                opening += 1;
            else {
                if (S.charAt(i - 1) == '(')
                    ret += 1 << (opening - 1);
                opening -= 1;
            }
        }

        return ret;
    }
}
