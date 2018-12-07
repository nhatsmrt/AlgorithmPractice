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
    public int countNodes(TreeNode root) {
        if (root == null)
            return 0;

        int height = height(root);
        int rightHeight = rightHeight(root);


        if (height == rightHeight)
            return power2(height) - 1;

        return 1 + countNodes(root.left) + countNodes(root.right);
    }


    private int power2(int n) {
        return 1 << n;
    }

    private int height(TreeNode root) {
        if (root == null)
            return 0;

        return 1 + height(root.left);
    }

    private int rightHeight(TreeNode root) {
        if (root == null)
            return 0;

        return 1 + rightHeight(root.right);
    }

}
