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
    public boolean checkLeft(TreeNode root, TreeNode left) {
        if (left == null)
            return true;

        if (root.val <= left.val)
            return false;

        return checkLeft(root, left.left) && checkLeft(root, left.right);
    }

    public boolean checkRight(TreeNode root, TreeNode right) {
        if (right == null)
            return true;

        if (root.val >= right.val)
            return false;

        return checkRight(root, right.left) && checkRight(root, right.right);
    }

    public boolean isValidBST(TreeNode root) {
        if (root == null)
            return true;


        if (!checkLeft(root, root.left))
            return false;


        if (!checkRight(root, root.right))
            return false;

        return isValidBST(root.left) && isValidBST(root.right);

    }
}
