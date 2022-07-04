/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public int maxDepth(Node root) {
        // Time Complexity: O(N)
        // Space Complexity: O(H)

        if (root == null)
            return 0;

        int ret = 0;
        for (Node child : root.children)
            ret = Math.max(ret, maxDepth(child));

        return ret + 1;
    }
}
