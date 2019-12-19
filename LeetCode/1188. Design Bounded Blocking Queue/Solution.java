class BoundedBlockingQueue {
    private int capacity;
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition enqueueCondition = lock.newCondition();
    private final Condition dequeueCondition = lock.newCondition();
    private Queue<Integer> data;

    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
        data = new LinkedList<Integer>();
    }

    public void enqueue(int element) throws InterruptedException {
        lock.lock();

        try {
            while(size() == capacity)
                enqueueCondition.await();

            data.add(element);
            if (size() == 1)
                dequeueCondition.signalAll();
        }
        finally {
            lock.unlock();
        }
    }

    public int dequeue() throws InterruptedException {
        lock.lock();
        int ret = -1;

        try {
            while (size() == 0)
                dequeueCondition.await();

            ret = data.remove();
            if (size() == capacity - 1)
                enqueueCondition.signalAll();

            return ret;
        }
        finally {
            lock.unlock();
        }

    }

    public int size() {
        return data.size();
    }
}
