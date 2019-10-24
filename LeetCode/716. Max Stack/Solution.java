class MaxStack {
    private Map<Integer, Stack<ListNode>> data;
    private ListNode front;
    private PriorityQueue<Integer> heap;

    /** initialize your data structure here. */
    public MaxStack() {
        data = new HashMap<Integer, Stack<ListNode>>();
        front = new ListNode(-1);
        heap = new PriorityQueue<Integer>();
    }

    public void push(int x) {
        heap.offer(-x);

        ListNode node = new ListNode(x);
        node.next = front.next;
        if (front.next != null)
            front.next.previous = node;
        node.previous = front;
        front.next = node;

        if (!data.containsKey(x))
            data.put(x, new Stack<ListNode>());
        data.get(x).push(node);
    }

    public int pop() {
        int removed = front.next.val;

        data.get(removed).pop();
        if (data.get(removed).size() == 0)
            data.remove(removed);

        if (front.next.next != null)
            front.next.next.previous = front;
        front.next = front.next.next;
        return removed;
    }

    public int top() {
        return front.next.val;
    }

    public int peekMax() {
        while (!data.containsKey(-heap.peek()))
            heap.poll();

        return -heap.peek();
    }

    public int popMax() {
        while (!data.containsKey(-heap.peek()))
            heap.poll();

        int max = -heap.poll();
        ListNode removeNode = data.get(max).pop();
        if (data.get(max).size() == 0)
            data.remove(max);
        removeNode.previous.next = removeNode.next;
        if (removeNode.next != null)
            removeNode.next.previous = removeNode.previous;

        return max;
    }

    private class ListNode {
        ListNode previous;
        ListNode next;
        int val;

        public ListNode(int num) {
            val = num;
        }

        public String toString() {
            return "" + val;
        }
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */
