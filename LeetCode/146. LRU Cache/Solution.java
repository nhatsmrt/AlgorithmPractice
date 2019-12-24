class LRUCache {
    private ListNode head;
    private ListNode tail;
    private Map<Integer, ListNode> data;
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        data = new HashMap<>();
        head = new ListNode();
        tail = new ListNode();

        head.next = tail;
        tail.previous = head;
    }

    public int get(int key) {
        // System.out.println(key);
        // System.out.println(data.containsKey(key));
        if (!data.containsKey(key))
            return -1;

        ListNode node = data.remove(key);
        remove(node);
        put(key, node.value);
        return node.value;
    }

    public void put(int key, int value) {
        if (data.containsKey(key)) {
            ListNode node = data.remove(key);
            remove(node);
            put(key, value);
        }
        else {
            if (data.size() == capacity) {
                ListNode toRemove = tail.previous;
                remove(toRemove);
                data.remove(toRemove.key);
            }

            ListNode node = new ListNode();
            node.key = key;
            node.value = value;
            ListNode next = head.next;

            head.next = node;
            node.previous = head;

            next.previous = node;
            node.next = next;

            data.put(key, node);
        }
        // System.out.println(data);
    }

    private void remove(ListNode node) {
        ListNode next = node.next;
        ListNode previous = node.previous;
        next.previous = previous;
        previous.next = next;
    }

    private class ListNode {
        ListNode next;
        ListNode previous;
        int key;
        int value;

        public String toString() {
            return key + " " + value;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
