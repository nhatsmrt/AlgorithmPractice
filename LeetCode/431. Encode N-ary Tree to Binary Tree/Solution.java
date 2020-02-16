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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Codec {

    // Encodes an n-ary tree to a binary tree.
    // Pairing Heap style
    public TreeNode encode(Node root) {
        return encode(root, new ArrayList<Node>(), 0);
    }

    private TreeNode encode(Node node, List<Node> siblings, int ind) {
        if (node == null)
            return null;

        TreeNode ret = new TreeNode(node.val);
        if (node.children != null && node.children.size() > 0)
            ret.left = encode(node.children.get(0), node.children, 0);
        else
            ret.left = null;

        if (ind + 1 < siblings.size())
            ret.right = encode(siblings.get(ind + 1), siblings, ind + 1);

        return ret;
    }

    // Decodes your binary tree to an n-ary tree.
    public Node decode(TreeNode root) {
        return decode(root, null);
    }

    private Node decode(TreeNode node, Node parent) {
        if (node == null)
            return null;

        Node ret = new Node(node.val);
        ret.children = new ArrayList<>();
        decode(node.left, ret);

        if (parent != null) {
            parent.children.add(ret);
            decode(node.right, parent);
        }

        return ret;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(root));
