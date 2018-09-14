class MyCircularDeque {
    int size = 0;
    int capacity;
    QueueNode root;

    /** Initialize your data structure here. Set the size of the deque to be k. */
    public MyCircularDeque(int k) {
        capacity = k;
    }

    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    public boolean insertFront(int value) {
        if (size >= capacity)
            return false;
        else if (root == null) {
            root = new QueueNode(value);
            root.next = root;
            root.previous = root;

            size = 1;
            return true;
        }

        QueueNode newRoot = new QueueNode(value);
        QueueNode rear = root.previous;
        newRoot.next = root;
        root.previous = newRoot;
        newRoot.previous = rear;
        rear.next = newRoot;

        root = newRoot;
        size += 1;
        return true;

    }

    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    public boolean insertLast(int value) {
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

    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    public boolean deleteFront() {
        if (size == 0)
            return false;
        else if (size == 1) {
            root = null;
            size = 0;
            return true;
        }

        QueueNode rear = root.previous;
        QueueNode newRoot = root.next;

        rear.next = newRoot;
        newRoot.previous = rear;
        root = newRoot;
        size -= 1;
        return true;
    }

    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    public boolean deleteLast() {
        if (size == 0)
            return false;
        else if (size == 1) {
            root = null;
            size = 0;
            return true;
        }

        QueueNode newRear = root.previous.previous;
        newRear.next = root;
        root.previous = newRear;
        size -= 1;
        return true;
    }

    /** Get the front item from the deque. */
    public int getFront() {
        if (root == null)
            return -1;
        else
            return root.val;
    }

    /** Get the last item from the deque. */
    public int getRear() {
        if (size == 0)
            return -1;
        else if (root.next == root)
            return root.val;
        else
            return root.previous.val;
    }

    /** Checks whether the circular deque is empty or not. */
    public boolean isEmpty() {
        return size == 0;
    }

    /** Checks whether the circular deque is full or not. */
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
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */
