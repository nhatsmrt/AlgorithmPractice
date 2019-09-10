class MyStack {
    private Queue<Integer> data;
    private int top;

    /** Initialize your data structure here. */
    public MyStack() {
        data = new LinkedList<Integer>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        data.add(x);
        top = x;
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        for (int i = 0; i < data.size() - 1; i++) {
            if (i == data.size() - 2);
                top = data.peek();
            data.add(data.remove());
        }
        return data.remove();
    }

    /** Get the top element. */
    public int top() {
        return top;
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return data.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
