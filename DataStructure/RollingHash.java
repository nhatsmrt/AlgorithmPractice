public class RollingHash {
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
