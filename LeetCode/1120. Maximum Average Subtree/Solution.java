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
    private double best;
    private int savedValue;
    private int savedCount;

    public double maximumAverageSubtree(TreeNode root) {
        best = -1;
        maximumAverageSubtreeRecursion(root);
        return best;
    }

    private void maximumAverageSubtreeRecursion(TreeNode node) {
        int value = node.val;
        int count = 1;

        if (node.left != null) {
            maximumAverageSubtreeRecursion(node.left);
            value += savedValue;
            count += savedCount;
        }

        if (node.right != null) {
            maximumAverageSubtreeRecursion(node.right);
            value += savedValue;
            count += savedCount;
        }

        savedValue = value;
        savedCount = count;

        double candidate = (float) (value) / count;
        if (candidate > best)
            best = candidate;
    }
}
