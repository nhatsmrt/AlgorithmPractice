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
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null)
            return 0;

        int candidate1 = diameterOfBinaryTree(root.left) + 1;
        int candidate2 = diameterOfBinaryTree(root.right) + 1;
        int candidate3 = height(root.left) + height(root.right) + 1;

        return Math.max(candidate1, Math.max(candidate2, candidate3)) - 1;
    }

    private int height (TreeNode root) {
        if (root == null)
            return 0;

        return 1 + Math.max(height(root.left), height(root.right));
    }
}
