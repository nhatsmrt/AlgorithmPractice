class MonotonicQueue {
    private Deque<List<Integer>> data;
    private int size;
    private int sum;

    public MonotonicQueue() {
        data = new LinkedList<List<Integer>>();
        size = 0;
        sum = 0;
    }

    public void add(int num) {
        List<Integer> entry = new ArrayList<Integer>();
        entry.add(num);
        entry.add(0);

        while (!data.isEmpty() && data.peekLast().get(0) >= num) {
            List<Integer> next = data.removeLast();
            entry.set(1, entry.get(1) + 1 + next.get(1));
            sum -= next.get(0) * (next.get(1) + 1);
        }
        data.addLast(entry);
        sum += (entry.get(0) * (entry.get(1) + 1));
        sum %= 1000000007;
        size += 1;
    }

    public void remove() {
        List<Integer> firstEntry = data.peekFirst();
        sum -= firstEntry.get(0);
        sum %= 1000000007;
        if (firstEntry.get(1) == 0)
            data.removeFirst();
        else
            firstEntry.set(1, firstEntry.get(1) - 1);
        size -= 1;
    }

    public int getMin() {
        return data.peekLast().get(0);
    }

    public boolean isEmpty() {
        return data.isEmpty();
    }

    public String toString() {
        return data.toString();
    }

    public int getSum() {
        return sum;
    }
}


class Solution {
    public int sumSubarrayMins(int[] A) {
        if (A.length == 1)
            return A[0];

        MonotonicQueue queue = new MonotonicQueue();
        int ret = 0;
        for (int i = A.length - 1; i >= 0; i--) {
            queue.add(A[i]);
            ret += queue.getSum();
            ret %= 1000000007;
        }

        return ret;

    }
}
