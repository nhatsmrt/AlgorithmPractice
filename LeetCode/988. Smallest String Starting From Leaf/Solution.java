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
    public String smallestFromLeaf(TreeNode root) {
        if (root == null)
            return "";

        String left = smallestFromLeaf(root.left);
        String right = smallestFromLeaf(root.right);
        String cur = toString(root.val);

        if (root.left == null && root.right == null)
            return toString(root.val);
        else if (root.right == null)
            return left + cur;
        else if (root.left == null)
            return right + cur;
        else if (left.compareTo(right) < 0)
            return left + cur;
        else
            return right + cur;
    }

    private String toString(int num) {
        return "" + (char) (num + 'a');
    }
}
