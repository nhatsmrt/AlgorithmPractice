class MinStack {
    private StackNode top;

    /** initialize your data structure here. */
    public MinStack() {}

    public void push(int x) {
        if (top == null) {
            top = new StackNode(x);
            top.min = x;
        }
        else {
            top = new StackNode(x, top);
            top.min = x < top.next.min ? x : top.next.min;
        }
    }

    public void pop() {
        top = top.next;
    }

    public int top() {
        return top.val;
    }

    public int getMin() {
        if (top == null)
            return -1;

        return top.min;
    }

    private class StackNode {
        public int val;
        public StackNode next;
        public int min;

        public StackNode(int val) { this(val, null); }

        public StackNode(int val, StackNode next) {
            this.val = val;
            this.next = next;
        }

    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
