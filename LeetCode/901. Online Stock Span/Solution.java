class MonotonicQueue {
    // monotonically increasing queue
    Deque<List<Integer>> data;

    public MonotonicQueue() {
        data = new LinkedList<List<Integer>>();
    }

    public int add (int value) {
        List<Integer> entry = new ArrayList<Integer>();
        entry.add(value);
        entry.add(0);

        while (!data.isEmpty() && data.peekLast().get(0) <= value) {
            List<Integer> next = data.removeLast();
            entry.set(1, entry.get(1) + 1 + next.get(1));
        }

        data.addLast(entry);
        return entry.get(1) + 1;
    }
}


class StockSpanner {
    MonotonicQueue queue;

    public StockSpanner() {
        queue = new MonotonicQueue();
    }

    public int next(int price) {
        return queue.add(price);
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */
