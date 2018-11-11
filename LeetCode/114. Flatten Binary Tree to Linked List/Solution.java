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
    public void flatten(TreeNode root) {
        if (root != null) {
            flatten(root.left);
            flatten(root.right);

            if (root.left != null) {
                TreeNode tmp = root.right;
                root.right = root.left;
                root.left = null;

                TreeNode par = root;
                while (par.right != null)
                    par = par.right;
                par.right = tmp;
            }
        }
    }
}
