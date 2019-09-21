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
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null || t == null)
            return s == null && t == null;

        if (equals(s, t))
            return true;

        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }

    private boolean equals(TreeNode s, TreeNode t) {
        if (s == null || t == null)
            return t == null && s == null;

        return s.val == t.val && equals(s.left, t.left) && equals(s.right, t.right);
    }
}
