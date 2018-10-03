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
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null)
            return new ArrayList<Integer>();

        List<Integer> ret = inorderTraversal(root.left);
        ret.add(root.val);
        List<Integer> right = inorderTraversal(root.right);
        ret.addAll(right);

        return ret;
    }
}
