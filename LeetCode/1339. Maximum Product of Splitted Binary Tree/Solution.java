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
    private Map<TreeNode, Integer> sums;
    private final int MOD = 1000000007;

    public int maxProduct(TreeNode root) {
        // Time Complexity; O(n)
        // Space Complexity: O(n)

        sums = new HashMap<>();
        return (int) (maxProduct(0, root) % MOD);
    }

    private long maxProduct(int cumsum, TreeNode node) {
        if (node == null)
            return 0;

        long candidate1 = maxProduct(cumsum + node.val + sum(node.right), node.left);
        long candidate2 = maxProduct(cumsum + node.val + sum(node.left), node.right);

        int sumLeft = sum(node.left);
        int sumRight = sum(node.right);

        cumsum += node.val;
        long candidate3 = (sumLeft + cumsum) * (long) sumRight;
        long candidate4 = (sumRight + cumsum) * (long) sumLeft;

        return Math.max(candidate1, Math.max(candidate2, Math.max(candidate3, candidate4)));
    }

    private int sum(TreeNode node) {
        if (node == null)
            return 0;

        if (sums.containsKey(node))
            return sums.get(node);

        int ret = node.val + sum(node.left) + sum(node.right);
        sums.put(node, ret);
        return ret;
    }
}
