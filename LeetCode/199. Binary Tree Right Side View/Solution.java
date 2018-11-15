/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ret = new ArrayList<Integer>();
        if (root == null)
            return ret;

        Deque<TreeNode> traversalDeque = new LinkedList<TreeNode>();
        traversalDeque.add(root);

        while (!traversalDeque.isEmpty()) {
            ret.add(traversalDeque.peekLast().val);
            int numNode = traversalDeque.size();

            for (int i = 0; i < numNode; i++) {
                TreeNode node = traversalDeque.removeFirst();
                if (node.left != null)
                    traversalDeque.addLast(node.left);
                if (node.right != null)
                    traversalDeque.addLast(node.right);
            }
        }

        return ret;
    }
}
