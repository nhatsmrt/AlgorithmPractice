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
    public int sumNumbers(TreeNode root) {
        if (root == null)
            return 0;

        return sumNumbers(root, 0);
    }

    private int sumNumbers(TreeNode root, int acc) {
        if (root.left == null && root.right == null)
            return acc * 10 + root.val;

        int ret = 0;
        if (root.left != null)
            ret += sumNumbers(root.left, acc * 10 + root.val);

        if (root.right != null)
            ret += sumNumbers(root.right, acc * 10 + root.val);

        return ret;

    }
}
