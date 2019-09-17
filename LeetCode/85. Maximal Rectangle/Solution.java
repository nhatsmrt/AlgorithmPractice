public class MonotonicQueue {
    private Deque<List<Integer>> data;

    public MonotonicQueue() {
        data = new LinkedList<List<Integer>>();
    }

    public int add(int value) {
        List<Integer> entry = new ArrayList<Integer>();
        entry.add(value);
        entry.add(0);
        while(!data.isEmpty() && data.peekLast().get(0) >= value) {
            List<Integer> next = data.removeLast();
            entry.set(1, entry.get(1) + next.get(1) + 1);
        }

        data.addLast(entry);
        int numElement = 0;
        int max = 0;

        Iterator<List<Integer>> it = data.descendingIterator();
        while(it.hasNext()) {
            List<Integer> next = it.next();
            numElement += next.get(1) + 1;
            if (next.get(0) * numElement > max)
                max = next.get(0) * numElement;
        }

        return max;
    }

    public String toString() {
        return data.toString();
    }
}


class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0)
            return 0;

        int[][] consec = new int[matrix.length][matrix[0].length];

        int maxArea = 0;
        for (int i = 0; i < matrix.length; i++) {
            MonotonicQueue queue = new MonotonicQueue();
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == '0')
                    consec[i][j] = 0;
                else {
                    consec[i][j] = 1;
                    if (i > 0)
                        consec[i][j] += consec[i - 1][j];
                }

                int candidate = queue.add(consec[i][j]);
                if (maxArea < candidate)
                    maxArea = candidate;
            }
        }

        return maxArea;
    }

}
