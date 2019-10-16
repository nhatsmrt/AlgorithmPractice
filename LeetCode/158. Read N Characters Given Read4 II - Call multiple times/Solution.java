/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char[] buf);
 */
public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    private Queue<Character> memory = new LinkedList<Character>();

    public int read(char[] buf, int n) {
        int to = Math.min(n, memory.size());
        int cur = 0;
        for (cur = 0; cur < to; cur++)
            buf[cur] = memory.remove();
        if (cur == n)
            return n;
        else {
            int numRead = n / 4;
            char[] tmp = new char[4];

            if (n % 4 != 0)
                numRead += 1;
            for (int i = 0; i < numRead; i++) {
                int res = read4(tmp);
                for (int j = 0; j < res; j++)
                    memory.add(tmp[j]);

                if (res < 4)
                    break;
            }

            to = Math.min(n - cur, memory.size());
            for (int i = 0; i < to; i++) {
                buf[cur] = memory.remove();
                cur += 1;
            }

            return cur;
        }

    }
}
