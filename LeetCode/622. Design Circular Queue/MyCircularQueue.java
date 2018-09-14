class MyCircularQueue {
    int size = 0;
    int capacity;
    QueueNode root;

    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        capacity = k;
    }

    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if (size >= capacity)
            return false;
        else if (root == null) {
            root = new QueueNode(value);
            root.next = root;
            root.previous = root;

            size = 1;
            return true;
        }
        else {
            QueueNode oldRear = root.previous;
            QueueNode newRear = new QueueNode(value);

            oldRear.next = newRear;
            newRear.previous = oldRear;
            newRear.next = root;
            root.previous = newRear;

            size += 1;
            return true;
        }
    }

    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if (root == null)
            return false;
        else if (root.next == root) {
            root = null;
            size -= 1;
            return true;
        }

        QueueNode rear = root.previous;
        QueueNode newRoot = root.next;
        root = newRoot;
        root.previous = rear;
        rear.next = root;

        size -= 1;
        return true;
    }

    /** Get the front item from the queue. */
    public int Front() {
        if (root == null)
            return -1;
        else
            return root.val;
    }

    /** Get the last item from the queue. */
    public int Rear() {
        if (root == null)
            return -1;
        else if (root.previous == root)
            return root.val;
        else
            return root.previous.val;
    }

    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        return size == 0;
    }

    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return size == capacity;
    }

    class QueueNode {
        int val;
        QueueNode next;
        QueueNode previous;

        public QueueNode(int val) {
            this.val = val;
        }
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
