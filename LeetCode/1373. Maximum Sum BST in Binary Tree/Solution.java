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
    private Map<TreeNode, Integer> dp;
    private Map<TreeNode, List<Integer>> ranges;

    public int maxSumBST(TreeNode root) {
        // Time and Space Complexity: O(N)

        if (root == null)
            return 0;

        dp = new HashMap<>();
        ranges = new HashMap<>();

        dfs(root);

        int ret = 0;
        for (TreeNode node : dp.keySet())
            ret = Math.max(ret, dp.get(node));

        return ret;
    }

    private void dfs(TreeNode node) {
        if (node != null) {
            dfs(node.left);
            dfs(node.right);

            boolean isBST = true;
            int lower = node.val;
            int upper = node.val;
            int totalVal = node.val;


            if (node.left != null) {
                if (dp.containsKey(node.left) && ranges.get(node.left).get(1) < node.val) {
                    lower = ranges.get(node.left).get(0);
                    totalVal += dp.get(node.left);
                }
                else
                    isBST = false;
            }

            if (node.right != null) {
                if (dp.containsKey(node.right) && ranges.get(node.right).get(0) > node.val) {
                    upper = ranges.get(node.right).get(1);
                    totalVal += dp.get(node.right);
                }
                else
                    isBST = false;
            }

            if (isBST) {
                dp.put(node, totalVal);
                List<Integer> range = new ArrayList<Integer>();
                range.add(lower);
                range.add(upper);
                ranges.put(node, range);
            }
        }
    }
}
