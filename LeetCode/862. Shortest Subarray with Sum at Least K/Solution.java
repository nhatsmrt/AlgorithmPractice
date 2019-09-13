class MonotonicQueue {
    private Deque<List<Integer>> data;
    private int maxDiff;
    private List<Integer> maxEntry;

    public MonotonicQueue(int maxDiff) {
        data = new LinkedList<List<Integer>>();
        this.maxDiff = maxDiff;
    }

    public void add(int num, int ind) {
        List<Integer> entry = new ArrayList<Integer>();
        entry.add(num);
        entry.add(ind);

        while (!isEmpty() && peekLast().get(0) <= num)
            removeLast();

        while (size() >= 2 && peekSecond().get(0) - num >= maxDiff)
            removeFirst();

        addLast(entry);
    }

    public void addLast(List<Integer> entry) {
        if (maxEntry == null)
            maxEntry = entry;
        else
            data.addLast(entry);
    }

    public List<Integer> peekLast() {
        if (data.isEmpty())
            return maxEntry;
        else
            return data.peekLast();
    }

    public List<Integer> removeLast() {
        List<Integer> ret;
        if (data.isEmpty()) {
            ret = maxEntry;
            maxEntry = null;
        }
        else
            ret = data.removeLast();
        return ret;
    }

    public List<Integer> removeFirst() {
        List<Integer> ret = maxEntry;
        if (data.isEmpty())
            maxEntry = null;
        else
            maxEntry = data.removeFirst();
        return ret;
    }

    public List<Integer> peekSecond() {
        return data.peekFirst();
    }

    public int getMax() {
        return maxEntry.get(0);
    }

    public int getMaxInd() {
        return maxEntry.get(1);
    }

    public boolean isEmpty() {
        return maxEntry == null;
    }

    public int size() {
        if (maxEntry == null)
            return 0;
        else
            return 1 + data.size();
    }
}


class Solution {
    public int shortestSubarray(int[] A, int K) {
        int[] prefixSum = new int[A.length + 1];
        prefixSum[0] = 0;
        for (int i = 1; i < prefixSum.length; i++)
            prefixSum[i] = prefixSum[i - 1] + A[i - 1];

        MonotonicQueue queue = new MonotonicQueue(K);
        int ret = -1;

        for (int i = prefixSum.length - 1; i >= 0; i--) {
            queue.add(prefixSum[i], i);
            if (queue.getMax() - prefixSum[i] >= K) {
                if (ret == -1 || queue.getMaxInd() - i < ret)
                ret = queue.getMaxInd() - i;
                queue.removeFirst();
            }
        }

        return ret;
    }
}
