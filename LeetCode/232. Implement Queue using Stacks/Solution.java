class MyQueue {
    private Stack<Integer> addStack;
    private Stack<Integer> removeStack;
    private int front;

    /** Initialize your data structure here. */
    public MyQueue() {
        addStack = new Stack<Integer>();
        removeStack = new Stack<Integer>();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        if (addStack.empty())
            front = x;
        addStack.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if (removeStack.empty()) {
            while(!addStack.empty())
                removeStack.push(addStack.pop());
        }
        return removeStack.pop();
    }

    /** Get the front element. */
    public int peek() {
        if (!removeStack.empty())
            return removeStack.peek();
        return front;
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return addStack.empty() && removeStack.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
