class AllOne {
    Map<String, Node> data;
    Node front;
    Node rear;

    /** Initialize your data structure here. */
    public AllOne() {
        data = new HashMap<String, Node>();
        front = new Node("");
        rear = new Node("");
        front.next = rear;
        rear.previous = front;
    }

    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    public void inc(String key) {
        if (data.containsKey(key)) {
            Node node = data.get(key);
            node.value += 1;
            while (node.next != rear && node.value > node.next.value) {
                Node prev = node.previous;
                Node next = node.next;
                Node nextNext = node.next.next;

                prev.next = next;

                node.next = nextNext;
                node.previous = next;

                next.next = node;
                next.previous = prev;

                nextNext.previous = node;
            }
        }
        else {
            Node node = new Node(key);
            node.value = 1;
            data.put(key, node);

            node.previous = front;
            node.next = front.next;
            front.next.previous = node;
            front.next = node;
        }
    }

    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    public void dec(String key) {
        if (data.containsKey(key)) {
            Node node = data.get(key);
            node.value -= 1;
            if (node.value == 0) {
                node.previous.next = node.next;
                node.next.previous = node.previous;
                data.remove(key);
            }
            else {
                if (node.previous != front && node.value < node.previous.value) {
                    Node prev = node.previous;
                    Node next = node.next;
                    Node prevPrev = node.previous.previous;

                    next.previous = prev;

                    node.next = prev;
                    node.previous = prevPrev;

                    prev.previous = node;
                    prev.next = next;

                    prevPrev.next = node;

                }
            }
        }
    }

    /** Returns one of the keys with maximal value. */
    public String getMaxKey() {
        return rear.previous.key;
    }

    /** Returns one of the keys with Minimal value. */
    public String getMinKey() {
        return front.next.key;
    }

    private void swap(Node node1, Node node2) {
        String tmpKey = node1.key;
        node1.key = node2.key;
        node2.key = tmpKey;

        int tmpVal = node1.value;
        node1.value = node2.value;
        node2.value = tmpVal;

        data.put(node1.key, node1);
        data.put(node2.key, node2);
    }

    private void printRear() {
        StringBuilder ret = new StringBuilder("[");
        Node it = rear.previous;
        while (it != front) {
            ret.append(it.toString() + ", ");
            it = it.previous;
        }
        ret.append("]");
        System.out.println(ret.toString());
    }

    private class Node {
        String key;
        int value;
        Node next;
        Node previous;

        public Node(String _key) {
            key = _key;
        }

        public String toString() {
            return key + " " + value;
        }
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param_3 = obj.getMaxKey();
 * String param_4 = obj.getMinKey();
 */
