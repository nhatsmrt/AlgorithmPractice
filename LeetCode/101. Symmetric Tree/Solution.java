a/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;

        return isSymmetricHelper(root.left, root.right);

    }

    private boolean isSymmetricHelper(TreeNode p, TreeNode q) {
        if (p == null)
            return q == null;
        if (q == null)
            return p == null;

        if (p.val != q.val)
            return false;

        return isSymmetricHelper(p.left, q.right) && isSymmetricHelper(p.right, q.left);
    }

}
