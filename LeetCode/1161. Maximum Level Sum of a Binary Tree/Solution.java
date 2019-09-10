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
    public int maxLevelSum(TreeNode root) {
        Queue<TreeNode> traverseQueue = new LinkedList<TreeNode>();
        traverseQueue.add(root);

        int argmax = 0;
        int curMax = 0;
        int level = 1;

        while (!traverseQueue.isEmpty()) {
            int levelSum = 0;
            int levelSize = traverseQueue.size();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = traverseQueue.remove();
                if (node.left != null)
                    traverseQueue.add(node.left);
                if (node.right != null)
                    traverseQueue.add(node.right);
                levelSum += node.val;
            }

            if (level == 1 || curMax < levelSum) {
                argmax = level;
                curMax = levelSum;
            }

            level += 1;
        }

        return argmax;
    }
}
