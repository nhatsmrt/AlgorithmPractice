class Solution {
    public void reverseWords(char[] s) {
        if (s.length > 0) {
            // Reverse the entire string
            reverse(s, 0, s.length - 1);
            int start = 0;
            int end = 0;

            // Find and reverse each word
            while (start < s.length) {
                while(end < s.length && s[end] != ' ')
                    end += 1;
                reverse(s, start, end - 1);
                start = end + 1;
                end = start;
            }
        }

    }

    private void reverse(char[] s, int start, int end) {
        int mid = (start + end) / 2;
        for (int i = start; i <= mid; i++) {
            char tmp = s[i];
            s[i] = s[end - i + start];
            s[end - i + start] = tmp;
        }
    }
}
