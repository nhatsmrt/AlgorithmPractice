/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> largestValues(TreeNode root) {
        if (root == null)
            return new ArrayList<>();

        List<TreeNode> curLevel = new ArrayList<>();
        curLevel.add(root);
        List<Integer> ret = new ArrayList<>();

        while (curLevel.size() > 0) {
            ret.add(curLevel.stream().map((node) -> node.val).max(Comparator.naturalOrder()).get());

            List<TreeNode> nextLevel = new ArrayList<>();
            for (TreeNode node : curLevel) {
                if (node.left != null)
                    nextLevel.add(node.left);

                if (node.right != null)
                    nextLevel.add(node.right);
            }

            curLevel = nextLevel;
        }

        return ret;
    }
}
