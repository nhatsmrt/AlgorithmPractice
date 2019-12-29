class Solution {
    private int[] ends;

    public int scoreOfParentheses(String S) {
        // O(n) time, O(n) space
        Stack<Integer> opening = new Stack<Integer>();
        ends = new int[S.length()];

        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == '(')
                opening.push(i);
            else {
                int start = opening.pop();
                ends[start] = i;
            }
        }

        return score(0, S.length() - 1);
    }

    private int score(int low, int high) {
        if (low == high - 1)
            return 1;

        int end = ends[low];
        if (end == high)
            return 2 * score(low + 1, high - 1);
        else
            return score(low, end) + score(end + 1, high);
    }
}
