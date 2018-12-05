/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;

    public Node() {}

    public Node(int _val,Node _prev,Node _next,Node _child) {
        val = _val;
        prev = _prev;
        next = _next;
        child = _child;
    }
};
*/
class Solution {
    public Node flatten(Node head) {
        if (head != null) {
            Node flatNext = flatten(head.next);
            if (head.child != null) {
                Node flatChild = flatten(head.child);
                head.next = flatChild;
                flatChild.prev = head;
                Node parLast = flatChild;
                while (parLast.next != null)
                    parLast = parLast.next;
                parLast.next = flatNext;
                if (flatNext != null)
                    flatNext.prev = parLast;
                head.child = null;
            }
            else {
                head.next = flatNext;
                if (flatNext != null)
                    flatNext.prev = head;
            }
        }
        return head;
    }
}
