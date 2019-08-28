class Solution {
    private class RollingHash {
        private int length;
        private long value;
        private int base;
        private int maxLength;

        public RollingHash(int base, int maxLength) {
            length = 0;
            value = 0;
            this.base = base;
            this.maxLength = maxLength;
        }

        public void addFront(char c) {
            if (length == maxLength)
                removeRear();

            value = value * base + ((long) (c - 'a') % base);
            length += 1;
        }

        public void removeFront() {
            if (length == 0)
                throw new IllegalArgumentException();
            value /= base;
            length -= 1;
        }

        public void addRear(char c) {
            if (length < maxLength) {
                value += ((long) (c - 'a') % base) * (long) (Math.pow(base, length));
                length += 1;
            }
        }

        public void removeRear() {
            if (length == 0)
                throw new IllegalArgumentException();
            value %= (long)(Math.pow(base, length - 1));
            length -= 1;
        }

        public long getHash() {
            return value;
        }

        public void clear() {
            length = 0;
            value = 0;
        }
    }

    public int longestDecomposition(String text) {
        RollingHash h1 = new RollingHash(31, 10);
        RollingHash h2 = new RollingHash(31, 10);

        int i = 0;
        int start = 0;
        int j = text.length() - 1;
        int end = text.length() - 1;

        int ret = 0;
        while (j >= i) {
            h1.addFront(text.charAt(i));
            h2.addRear(text.charAt(j));

            if (j == i + 1) {
                if (checkEqual(text, start, i, j, end))
                    ret += 2;
                else
                    ret += 1;
            }
            else if (j == i)
                ret += 1;
            else {
                if (h1.getHash() == h2.getHash() && checkEqual(text, start, i, j, end)) {
                    ret += 2;
                    start = i + 1;
                    end = j - 1;
                    h1.clear();
                    h2.clear();
                }
            }

            i += 1;
            j -= 1;
        }

        return ret;
    }

    private boolean checkEqual(String str, int start, int i, int j, int end) {
        if (i - start != end - j || i < start || j > end)
            throw new IllegalArgumentException();


        for (int k = 0; k < i - start + 1; k++) {
            if (str.charAt(start + k) != str.charAt(j + k))
                return false;
        }

        return true;
    }
}
