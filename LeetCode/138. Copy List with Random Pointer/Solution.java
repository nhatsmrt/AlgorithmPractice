/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
    private Map<Node, Node> copyMap;

    public Node copyRandomList(Node head) {
        copyMap = new HashMap<Node, Node>();
        return copyRandomListRecursion(head);
    }

    public Node copyRandomListRecursion(Node node) {
        if (node == null)
            return null;


        if (copyMap.containsKey(node))
            return copyMap.get(node);

        Node ret = new Node(node.val, null, null);
        copyMap.put(node, ret);

        ret.next = copyRandomListRecursion(node.next);
        ret.random = copyRandomListRecursion(node.random);


        return ret;
    }
}
