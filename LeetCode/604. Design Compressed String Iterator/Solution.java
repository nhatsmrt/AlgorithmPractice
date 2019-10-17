class StringIterator {
    private int it;
    private int next;
    private int cnt;
    private String compressedString;

    public StringIterator(String compressedString) {
        this.compressedString = compressedString;
        it = 0;
        cnt = getCount(1);
    }

    public char next() {
        if (hasNext()) {
            char ret = compressedString.charAt(it);
            cnt -= 1;
            if (cnt == 0) {
                it = next;
                if (it < compressedString.length())
                    cnt = getCount(next + 1);
                else
                    cnt = -1;
            }

            return ret;
        }
        else
            return ' ';
    }

    public boolean hasNext() {
        return cnt > 0;
    }

    private int getCount(int start) {
        cnt = 0;
        while (
            start < compressedString.length() &&
            compressedString.charAt(start) >= '0' &&
            compressedString.charAt(start) <= '9'
        ) {
            cnt = cnt * 10 + (int) (compressedString.charAt(start) - '0');
            start += 1;
        }

        next = start;
        return cnt;
    }
}

/**
 * Your StringIterator object will be instantiated and called as such:
 * StringIterator obj = new StringIterator(compressedString);
 * char param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
