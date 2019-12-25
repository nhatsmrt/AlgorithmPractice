class LFUCache {
    // References:
    // http://dhruvbird.com/lfu.pdf
    // https://ieftimov.com/post/when-why-least-frequently-used-cache-implementation-golang/

    private Map<Integer, ItemNode> data;
    private FrequencyNode head;
    private FrequencyNode tail;
    private int capacity;

    public LFUCache(int capacity) {
        data = new HashMap<>();
        head = new FrequencyNode();
        tail = new FrequencyNode();

        head.next = tail;
        tail.previous = head;
        this.capacity = capacity;
    }

    public int get(int key) {
        if (capacity == 0 || !data.containsKey(key))
            return -1;

        ItemNode itemNode = data.get(key);
        increaseFrequency(itemNode);
        return itemNode.value;
    }

    public void put(int key, int value) {
        if (capacity > 0) {
            if (data.containsKey(key)) {
                ItemNode itemNode = data.get(key);
                itemNode.value = value;
                increaseFrequency(itemNode);
            }
            else {
                ItemNode itemNode = new ItemNode();
                itemNode.key = key;
                itemNode.value = value;

                if (data.size() == capacity)
                    evict();

                data.put(key, itemNode);
                if (head.next != tail && head.next.frequency == 0) {
                    insert(head.next, itemNode);
                }
                else {
                    FrequencyNode newFreqNode = new FrequencyNode();
                    newFreqNode.frequency = 0;
                    insert(newFreqNode, itemNode);

                    FrequencyNode oldNext = head.next;
                    head.next = newFreqNode;
                    newFreqNode.previous = head;
                    oldNext.previous = newFreqNode;
                    newFreqNode.next = oldNext;
                }

            }
        }
    }

    private void evict() {
        if (head.next != tail) {
            FrequencyNode freqNode = head.next;
            data.remove(freqNode.tail.previous.key);
            removeItemNode(freqNode.tail.previous);
            if (isEmpty(freqNode))
                removeFreqNode(freqNode);
        }
    }

    private void removeItemNode(ItemNode node) {
        ItemNode next = node.next;
        ItemNode previous = node.previous;

        next.previous = previous;
        previous.next = next;
    }

    private void removeFreqNode(FrequencyNode node) {
        FrequencyNode next = node.next;
        FrequencyNode previous = node.previous;

        next.previous = previous;
        previous.next = next;
    }

    private boolean isEmpty(FrequencyNode node) { return node.head.next == node.tail;}

    private void increaseFrequency(ItemNode itemNode) {
        removeItemNode(itemNode);
        FrequencyNode freqNode = itemNode.freqNode;
        if (freqNode.next != tail && freqNode.next.frequency == freqNode.frequency + 1)
            insert(freqNode.next, itemNode);
        else {
            FrequencyNode nextFreqNode = new FrequencyNode();
            nextFreqNode.frequency = freqNode.frequency + 1;

            FrequencyNode oldNext = freqNode.next;
            freqNode.next = nextFreqNode;
            nextFreqNode.previous = freqNode;
            nextFreqNode.next = oldNext;
            oldNext.previous = nextFreqNode;

            insert(nextFreqNode, itemNode);
        }

        if (isEmpty(freqNode))
            removeFreqNode(freqNode);
    }

    private void insert(FrequencyNode freqNode, ItemNode itemNode) {
        itemNode.freqNode = freqNode;
        ItemNode next = freqNode.head.next;

        freqNode.head.next = itemNode;
        itemNode.previous = freqNode.head;
        next.previous = itemNode;
        itemNode.next = next;
    }

    private class FrequencyNode {
        int frequency;
        ItemNode head;
        ItemNode tail;
        FrequencyNode next;
        FrequencyNode previous;

        public FrequencyNode() {
            head = new ItemNode();
            tail = new ItemNode();

            head.next = tail;
            tail.previous = head;
        }
    }

    private class ItemNode {
        int key;
        int value;
        FrequencyNode freqNode;
        ItemNode next;
        ItemNode previous;

        public String toString() {
            return key + " " + value + " " + freqNode.frequency;
        }
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
