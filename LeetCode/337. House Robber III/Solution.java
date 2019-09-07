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
    private Map<TreeNode, Integer> dpMap;

    public int rob(TreeNode root) {
        dpMap = new HashMap<TreeNode, Integer>();
        return robDP(root);
    }

    private int robDP(TreeNode node) {
        if (node == null)
            return 0;

        if (dpMap.containsKey(node))
            return dpMap.get(node);

        int candidate1 = robDP(node.left) + robDP(node.right);
        int candidate2 = node.val;
        if (node.left != null)
            candidate2 += robDP(node.left.left) + robDP(node.left.right);
        if (node.right != null)
            candidate2 += robDP(node.right.left) + robDP(node.right.right);

        int ret = candidate1 > candidate2 ? candidate1 : candidate2;
        dpMap.put(node, ret);
        return ret;
    }
}
